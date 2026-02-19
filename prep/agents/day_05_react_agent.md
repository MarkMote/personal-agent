# Day 5: ReAct Agent from Scratch (~2 hrs)

**Goal:** Build a ReAct (Reason + Act) agent without the Anthropic API - using an injected LLM callable. This tests your understanding of the agent loop pattern independently of any SDK. Also build an async variant with timeouts.

---

## Reading (20 min)

1. **ReAct pattern** - The core idea:
   - Agent alternates: **Thought** (reason about what to do) -> **Action** (call a tool) -> **Observation** (get the result) -> repeat
   - Stops when it reaches a **Final Answer**
   - The LLM drives the loop by generating structured text that gets parsed

2. **Review problems:**
   - Problem 9 in `../interview_problems/original/01_applied_ai.md` - ReAct agent with injected LLM
   - Problem 14 - Async tool-calling agent with timeouts and JSON parsing

3. **Why this matters for the interview:**
   - Shows you understand the pattern *conceptually*, not just the SDK wrapper
   - The interviewer may give you a mock LLM function instead of API access
   - Async + error handling shows production awareness

---

## Project A: ReAct Agent with Injected LLM (45 min)

### The Problem

Build a ReAct agent where the LLM is injected as a callable. No API needed.

```python
import re
from typing import Callable

class ReActAgent:
    def __init__(self, llm: Callable[[str], str]):
        """
        llm: takes a prompt string, returns a response string.
        Could be a real API call or a mock for testing.
        """
        self.llm = llm
        self.tools = {
            "search": self._search,
            "calculate": self._calculate,
        }

    def _search(self, query: str) -> str:
        """Mock search - in production this would be a real search API."""
        mock_results = {
            "capital of france": "Paris is the capital city of France.",
            "population of tokyo": "Tokyo has a population of approximately 13.96 million.",
            "square root 16": "The square root of 16 is 4.",
        }
        query_lower = query.lower().strip('"').strip("'")
        for key, value in mock_results.items():
            if key in query_lower:
                return value
        return f"No results found for: {query}"

    def _calculate(self, expr: str) -> str:
        """Safe calculator for simple arithmetic."""
        try:
            # Only allow safe math characters
            allowed = set("0123456789+-*/.() ")
            if not all(c in allowed for c in expr):
                return f"Error: unsafe expression"
            return str(eval(expr))
        except Exception as e:
            return f"Error: {str(e)}"

    def _parse_action(self, text: str):
        """Parse 'Action: tool_name(arg)' from LLM output."""
        match = re.search(r'^Action:\s*(\w+)\((.+?)\)$', text, re.MULTILINE)
        if match:
            return match.group(1), match.group(2).strip('"').strip("'")
        return None, None

    def run(self, prompt: str, max_steps: int = 5) -> str:
        """
        Run the ReAct loop:
        1. Append user prompt
        2. Get Thought from LLM
        3. Parse Action
        4. Execute tool -> Observation
        5. Repeat until Final Answer or max_steps
        """
        transcript = f"Question: {prompt}\n"

        for step in range(max_steps):
            # Ask LLM for next thought + action
            response = self.llm(transcript)
            transcript += response + "\n"

            # Check for final answer
            for line in response.split("\n"):
                if line.strip().lower().startswith("final answer:"):
                    return line.split(":", 1)[1].strip()

            # Parse action
            tool_name, tool_arg = self._parse_action(response)
            if tool_name is None:
                # No action found - ask LLM to continue
                transcript += "Observation: Please provide an Action in the format: Action: tool_name(arg)\n"
                continue

            # Execute tool
            if tool_name not in self.tools:
                observation = f"Error: Unknown tool '{tool_name}'. Available: {list(self.tools.keys())}"
            else:
                observation = self.tools[tool_name](tool_arg)

            transcript += f"Observation: {observation}\n"
            print(f"  Step {step+1}: {tool_name}({tool_arg}) -> {observation}")

        raise RuntimeError("max steps")
```

### Test with a Mock LLM

```python
# Simple mock LLM that follows a script
class MockLLM:
    def __init__(self, responses):
        self.responses = iter(responses)

    def __call__(self, prompt):
        return next(self.responses)

# Test: "What is 3 + the capital of France?"
mock = MockLLM([
    "Thought: I need to find the capital of France first.\nAction: search(capital of France)",
    "Thought: The capital is Paris. Now I need to figure out what 3 + Paris means. Since this doesn't make mathematical sense, I'll just say 3.\nFinal Answer: The capital of France is Paris, and 3 + Paris doesn't compute mathematically.",
])

agent = ReActAgent(llm=mock)
answer = agent.run("What is 3 + the capital of France?")
print(f"Answer: {answer}")
```

### Test with a real LLM (if you have API access)

```python
import anthropic
client = anthropic.Anthropic()

def real_llm(prompt: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system="""You are a ReAct agent. For each step, output:
Thought: <your reasoning>
Action: tool_name(argument)

Available tools: search(query), calculate(expression)
When you have the final answer, output: Final Answer: <answer>""",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

agent = ReActAgent(llm=real_llm)
answer = agent.run("What is the square root of 16 times 5?")
print(f"Answer: {answer}")
```

---

## Project B: Async Agent with Timeouts (45 min)

### The Problem (from Problem 14)

Build an async agent that parses JSON tool calls, handles timeouts, and manages error cases.

```python
import asyncio
import json
import re
from typing import Callable, Awaitable
from pydantic import BaseModel, ValidationError

class ToolCall(BaseModel):
    tool: str
    input: dict

class AsyncToolAgent:
    def __init__(
        self,
        llm: Callable[[str], Awaitable[str]],
        tools: dict[str, Callable],
        timeout: float = 5.0
    ):
        self.llm = llm
        self.tools = tools
        self.timeout = timeout

    def _extract_json(self, text: str) -> dict | None:
        """Extract the first JSON object from text."""
        match = re.search(r'\{[^{}]*\}', text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                return None
        return None

    async def _execute_tool(self, name: str, input_data: dict) -> str:
        """Execute a tool with timeout."""
        if name not in self.tools:
            return f"Tool not found: {name}"

        try:
            func = self.tools[name]
            if asyncio.iscoroutinefunction(func):
                result = await asyncio.wait_for(func(**input_data), timeout=self.timeout)
            else:
                result = await asyncio.wait_for(
                    asyncio.get_event_loop().run_in_executor(None, lambda: func(**input_data)),
                    timeout=self.timeout
                )
            return str(result)
        except asyncio.TimeoutError:
            return f"Tool error: {name} timed out after {self.timeout}s"
        except Exception as e:
            return f"Tool error: {str(e)}"

    async def run(self, prompt: str, max_steps: int = 10) -> str:
        transcript = f"Question: {prompt}\n"

        for step in range(max_steps):
            response = await self.llm(transcript)
            transcript += response + "\n"

            # Check for final answer
            for line in response.split("\n"):
                if line.strip().lower().startswith("answer:"):
                    return line.split(":", 1)[1].strip()

            # Try to extract JSON tool call
            json_data = self._extract_json(response)
            if json_data is None:
                transcript += "Observation: Invalid JSON - please use format: {\"tool\": \"name\", \"input\": {\"arg\": \"value\"}}\n"
                continue

            # Validate with Pydantic
            try:
                tool_call = ToolCall(**json_data)
            except ValidationError as e:
                transcript += f"Observation: Invalid tool call format: {e}\n"
                continue

            # Execute
            observation = await self._execute_tool(tool_call.tool, tool_call.input)
            transcript += f"Observation: {observation}\n"
            print(f"  Step {step+1}: {tool_call.tool}({tool_call.input}) -> {observation[:100]}")

        raise RuntimeError("max steps")
```

### Test It

```python
# Mock async tools
async def async_search(query: str) -> str:
    await asyncio.sleep(0.1)  # Simulate network delay
    return f"Search result for '{query}': Some relevant information."

async def slow_tool(query: str) -> str:
    await asyncio.sleep(10)  # Will timeout
    return "This should never return"

# Mock async LLM
async def mock_async_llm(prompt: str) -> str:
    if "Observation" not in prompt:
        return 'Thought: I need to search for information.\n{"tool": "search", "input": {"query": "test"}}'
    else:
        return "Answer: Based on the search, the answer is 42."

agent = AsyncToolAgent(
    llm=mock_async_llm,
    tools={"search": async_search, "slow_tool": slow_tool},
    timeout=2.0
)

# Run it
result = await agent.run("What is the meaning of life?")
print(f"Result: {result}")
```

---

## Drills (10 min)

1. **Regex parsing** - Write a regex to extract `tool_name(arg)` from "Action: search(capital of France)". Do it from memory.

2. **JSON extraction** - Write code to find and parse the first `{...}` in a string. Handle malformed JSON.

3. **Async timeout** - Write `asyncio.wait_for(coro, timeout=5.0)` with a try/except for TimeoutError.

---

## Key Takeaways

- ReAct is the conceptual pattern behind all agent loops: Think -> Act -> Observe -> Repeat
- **Injected LLM** decouples the agent logic from the API - makes it testable
- **Pydantic validation** for tool calls catches malformed inputs before execution
- **Async + timeouts** prevents runaway tools from blocking forever
- Always return an observation even on error - the LLM needs it to continue
- The ReAct pattern works with OR without the Anthropic SDK - understand both
