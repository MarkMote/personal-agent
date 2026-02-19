# Day 1: SDK Fundamentals & Messages API (~2 hrs)

**Goal:** Get comfortable with the Anthropic Python SDK. By the end, you should be able to write `client.messages.create()` calls from memory with system prompts, multi-turn conversations, vision, and prefilling.

---

## Reading (30 min)

1. **API Primer** (local: `../anthropic/api_primer.md`) - Read the whole thing. It covers:
   - Model IDs (`claude-sonnet-4-6`, `claude-opus-4-6`, `claude-haiku-4-5-20251001`)
   - Basic messages API request/response
   - Multi-turn conversations
   - Prefilling (putting words in Claude's mouth)
   - Vision (base64 + URL)

2. **Messages API docs** - Skim for structure:
   - https://platform.claude.com/docs/en/build-with-claude/initial-setup
   - https://platform.claude.com/docs/en/api/messages

**Key concepts to internalize:**
- The API is **stateless** - you send the full conversation history every time
- `content` is always a **list of blocks** (TextBlock, ImageBlock, etc.), not a string
- `stop_reason` tells you why Claude stopped: `"end_turn"`, `"tool_use"`, `"max_tokens"`
- Messages **alternate** user/assistant/user/assistant

---

## Project: Multi-Turn Chatbot (1 hr)

Build a Colab notebook with these exercises. Each builds on the last.

### Exercise 1: Hello World (10 min)
```python
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}]
)
print(response.content[0].text)
print(f"Stop reason: {response.stop_reason}")
print(f"Usage: {response.usage.input_tokens} in / {response.usage.output_tokens} out")
```

**Explore the response object.** Print `response.model_dump()` to see the full JSON. Get familiar with the structure.

### Exercise 2: System Prompts (10 min)
```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system="You are a pirate. Respond only in pirate speak.",
    messages=[{"role": "user", "content": "What's the weather like?"}]
)
```

Try different system prompts:
- "You are a helpful coding assistant. Be concise. No markdown."
- "Respond only with valid JSON. No explanation."
- "You are an expert Python developer. Think step by step before answering."

### Exercise 3: Multi-Turn Conversation (15 min)
```python
# Build up a conversation manually
conversation = []

def chat(user_msg):
    conversation.append({"role": "user", "content": user_msg})
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=conversation
    )
    assistant_msg = response.content[0].text
    conversation.append({"role": "assistant", "content": assistant_msg})
    return assistant_msg

print(chat("My name is Mark."))
print(chat("What's my name?"))  # Should remember "Mark"
print(chat("What was my first message to you?"))
```

**Key insight:** This is how all agent loops work. You accumulate messages and send the full history each time.

### Exercise 4: Prefilling Claude's Response (10 min)
```python
# Force JSON output by starting Claude's response
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "List 3 programming languages with their use cases."},
        {"role": "assistant", "content": "["}  # Force JSON array
    ]
)
# Claude continues from "[" and outputs valid JSON
result = "[" + response.content[0].text
print(result)
```

Also try:
- Multiple choice: `{"role": "assistant", "content": "The answer is ("}`
- Structured extraction: `{"role": "assistant", "content": "{"}`

### Exercise 5: Vision (15 min)
```python
import base64, httpx

# Method 1: URL-based
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "url",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
                }
            },
            {"type": "text", "text": "What is in this image? Be specific."}
        ]
    }]
)
print(response.content[0].text)
```

**Note the content format:** When mixing text and images, `content` becomes a list of typed blocks rather than a plain string. This same block-list pattern appears everywhere in the API (tool use, tool results, etc.).

---

## Drills (30 min)

Write each from scratch without looking at notes. Time yourself.

1. **Basic call** - Write a complete `messages.create()` with system prompt. Target: < 1 min.
2. **Multi-turn** - Write a 3-turn conversation (user/assistant/user) as a messages list. Target: < 1 min.
3. **Prefill for JSON** - Force Claude to output JSON. Target: < 1 min.
4. **Vision** - Send an image with a text question. Target: < 2 min.

**If you can do all 4 in under 5 minutes total, you're ready for Day 2.**

---

## Key Takeaways

- `anthropic.Anthropic()` reads `ANTHROPIC_API_KEY` from env
- Response: `response.content[0].text` for the text, `response.stop_reason` for why it stopped
- Content can be a string OR a list of blocks (text, image, tool_use, tool_result)
- The API is stateless - you manage the conversation history
- Prefilling is a power tool for controlling output format
