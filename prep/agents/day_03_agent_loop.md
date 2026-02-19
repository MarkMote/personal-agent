# Day 3: The Agent Loop (~2 hrs)

**Goal:** Build the complete agent loop pattern from scratch. This is THE core deliverable for the interview. By the end, you should be able to write `run_agent()` from memory in under 5 minutes.

---

## Reading (20 min)

1. **"Building Effective Agents" blog** (MUST READ - this is cultural alignment)
   - https://www.anthropic.com/engineering/building-effective-agents
   - Key takeaway: **start simple, only add complexity when it measurably helps**
   - Complexity ladder: augmented LLM -> prompt chaining -> routing -> parallelization -> orchestrator-workers -> evaluator-optimizer -> autonomous agents
   - "Agents are the last resort" - say this in the interview if a simpler pattern suffices

2. **Cheat sheet** (local: `../anthropic_agents.md`) - Review the agent loop section

**Anthropic's definition of an "agent":**
> A system where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. The LLM decides on each step based on the results of previous actions.

---

## The Core Pattern: `run_agent()`

This is the most important code you'll write in the interview. Know it cold.

```python
import anthropic

client = anthropic.Anthropic()

def run_agent(user_message, tools, tool_functions, system=None, max_turns=10):
    """
    The canonical agent loop. Send a message, process tool calls, repeat.
    """
    messages = [{"role": "user", "content": user_message}]

    for _ in range(max_turns):
        # Build the API call
        kwargs = {
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 4096,
            "tools": tools,
            "messages": messages,
        }
        if system:
            kwargs["system"] = system

        response = client.messages.create(**kwargs)

        # If model is done (no more tool calls), return final text
        if response.stop_reason == "end_turn":
            # Extract text from content blocks
            return "".join(
                block.text for block in response.content
                if hasattr(block, "text")
            )

        # Add assistant's full response to conversation
        messages.append({"role": "assistant", "content": response.content})

        # Execute each tool call and collect results
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                try:
                    func = tool_functions[block.name]
                    result = func(**block.input)
                except Exception as e:
                    result = f"Error: {str(e)}"

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result)
                })

        # Feed results back as a user message
        messages.append({"role": "user", "content": tool_results})

    return "Max turns reached"
```

### Why each part matters:
- **`response.content`** (not just text): The assistant message may contain both text AND tool_use blocks. You must pass ALL of them back.
- **`tool_use_id` matching**: Each tool_result must reference the exact id from the corresponding tool_use block.
- **Error wrapping**: Always return a tool_result even on error. Claude needs it to continue the conversation.
- **`max_turns` guard**: Prevents infinite loops if the model keeps calling tools.
- **Text extraction at end**: Response may have multiple text blocks; join them.

---

## Project: File Q&A Agent (1 hr)

Build an agent that can explore a directory structure and answer questions about files.

### Step 1: Define Tools (15 min)
```python
import os, json

tools = [
    {
        "name": "list_directory",
        "description": "List all files and subdirectories in a given directory path. Returns a JSON array of filenames. Use this to explore the filesystem.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Directory path to list, e.g. '.' or './src'"
                }
            },
            "required": ["path"]
        }
    },
    {
        "name": "read_file",
        "description": "Read the full contents of a text file. Returns the file content as a string. Use this to examine file contents.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Path to the file to read"
                }
            },
            "required": ["path"]
        }
    },
    {
        "name": "count_lines",
        "description": "Count the number of lines in a file. Returns an integer. Useful for comparing file sizes.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Path to the file"
                }
            },
            "required": ["path"]
        }
    }
]

def list_directory(path):
    entries = os.listdir(path)
    return json.dumps(sorted(entries))

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def count_lines(path):
    with open(path, 'r') as f:
        return len(f.readlines())

tool_functions = {
    "list_directory": list_directory,
    "read_file": read_file,
    "count_lines": count_lines,
}
```

### Step 2: Create Test Files (5 min)
```python
# Create a small test directory in Colab
os.makedirs("test_project/src", exist_ok=True)

with open("test_project/README.md", "w") as f:
    f.write("# Test Project\nA sample project for testing.\n")

with open("test_project/src/main.py", "w") as f:
    f.write("""def hello():\n    print("Hello world")\n\ndef add(a, b):\n    return a + b\n\ndef multiply(a, b):\n    return a * b\n\nif __name__ == "__main__":\n    hello()\n""")

with open("test_project/src/utils.py", "w") as f:
    f.write("""import os\n\ndef read_config(path):\n    with open(path) as f:\n        return f.read()\n""")
```

### Step 3: Run the Agent (15 min)
```python
system_prompt = """You are a helpful file analysis agent. When asked about files,
use the tools to explore the filesystem and answer accurately. Always verify your
answers by reading the actual files rather than guessing."""

# Test queries
queries = [
    "What files are in the test_project directory?",
    "Which Python file in test_project/src has the most functions?",
    "What does the README say about this project?",
]

for q in queries:
    print(f"\n{'='*60}")
    print(f"Q: {q}")
    answer = run_agent(q, tools, tool_functions, system=system_prompt)
    print(f"A: {answer}")
```

### Step 4: Add Observability (15 min)

Modify `run_agent` to print each step. In an interview, showing your agent's reasoning is a win.

```python
def run_agent_verbose(user_message, tools, tool_functions, system=None, max_turns=10):
    messages = [{"role": "user", "content": user_message}]

    for turn in range(max_turns):
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            tools=tools,
            messages=messages,
            **({"system": system} if system else {})
        )

        print(f"\n--- Turn {turn + 1} | stop_reason: {response.stop_reason} ---")

        # Print any text blocks (Claude's reasoning)
        for block in response.content:
            if hasattr(block, "text"):
                print(f"  [Think] {block.text[:200]}...")

        if response.stop_reason == "end_turn":
            final = "".join(b.text for b in response.content if hasattr(b, "text"))
            print(f"  [Final] {final}")
            return final

        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"  [Tool] {block.name}({json.dumps(block.input)})")
                try:
                    result = tool_functions[block.name](**block.input)
                except Exception as e:
                    result = f"Error: {str(e)}"
                print(f"  [Result] {str(result)[:200]}")
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result)
                })

        messages.append({"role": "user", "content": tool_results})

    return "Max turns reached"
```

### Step 5: Edge Cases (10 min)

Test these scenarios and verify the agent handles them:
```python
# Tool error case
print(run_agent_verbose("Read the file nonexistent.txt", tools, tool_functions, system=system_prompt))

# Multi-step reasoning
print(run_agent_verbose(
    "Compare test_project/src/main.py and test_project/src/utils.py. Which has more lines?",
    tools, tool_functions, system=system_prompt
))
```

---

## Drill: Write `run_agent` from Memory (30 min)

**This is the most important drill.** Close all notes and write the agent loop from scratch.

1. **Attempt 1** (10 min): Write `run_agent(user_message, tools, tool_functions, max_turns=10)` from memory. Then compare with the reference above.

2. **Attempt 2** (5 min): Fix any mistakes from attempt 1. Write it again.

3. **Attempt 3** (5 min): Write it one more time. Should be < 3 minutes now.

4. **Speed test** (remaining time): Start a timer. Write the complete function. Target: **under 5 minutes.** This is what you need for the interview.

### Checklist - did you remember:
- [ ] `messages` list starting with user message
- [ ] `for _ in range(max_turns)` loop
- [ ] `client.messages.create()` with model, max_tokens, tools, messages
- [ ] Check `response.stop_reason == "end_turn"` for completion
- [ ] `messages.append({"role": "assistant", "content": response.content})`
- [ ] Loop through `response.content` for `block.type == "tool_use"`
- [ ] Try/except around tool execution
- [ ] `tool_results` list with `type`, `tool_use_id`, `content`
- [ ] `messages.append({"role": "user", "content": tool_results})`
- [ ] Return "Max turns reached" as fallback

---

## Key Takeaways

- The agent loop is: **send -> check stop_reason -> execute tools -> feed results back -> repeat**
- Always include the full `response.content` in the assistant message (not just text)
- Always return a `tool_result` for every `tool_use`, even on error
- Add observability (print statements) - interviewers want to see the agent's reasoning
- **In the interview:** Get the basic loop working first. Polish later.
