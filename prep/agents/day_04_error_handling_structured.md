# Day 4: Error Handling & Structured Output (~2 hrs)

**Goal:** Harden the agent loop with production-grade error handling, parallel tool calls, and structured output. These are the details that separate a working demo from a production system.

---

## Reading (30 min)

1. **Structured Outputs** - https://platform.claude.com/docs/en/build-with-claude/structured-outputs
   - Two features: JSON outputs (`output_config.format`) and strict tool use (`strict: true`)
   - `strict: true` on tool definitions guarantees schema validation
   - JSON schema output for forcing structured responses

2. **Tool use best practices** (from implement-tool-use docs):
   - Detailed descriptions > brief ones (this is "the single most important factor")
   - `input_examples` field (beta) for complex tools
   - `tool_choice` for controlling when tools are used

3. **Parallel tool use** - Claude may call multiple tools in a single response. Your loop must handle this.

---

## Project: Robust Data Agent (1 hr 15 min)

Build an agent with multiple tools, error handling, parallel tool calls, and structured output.

### Step 1: Define Tools with Strict Schemas (15 min)

```python
import anthropic, json

client = anthropic.Anthropic()

tools = [
    {
        "name": "get_stock_price",
        "description": "Get the current stock price for a publicly traded company. Takes a ticker symbol (e.g., 'AAPL' for Apple). Returns the price in USD. Only works for major US exchanges (NYSE, NASDAQ). Will error if the ticker is invalid.",
        "input_schema": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": "Stock ticker symbol, e.g. 'AAPL', 'GOOGL', 'MSFT'"
                }
            },
            "required": ["ticker"]
        }
    },
    {
        "name": "get_company_info",
        "description": "Get basic information about a company including sector, market cap, and description. Takes a ticker symbol. Use this for background research before making comparisons.",
        "input_schema": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": "Stock ticker symbol"
                }
            },
            "required": ["ticker"]
        }
    },
    {
        "name": "calculate",
        "description": "Evaluate a mathematical expression. Supports basic arithmetic: +, -, *, /, **, (). Use this for computations like percentage change, ratios, etc.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Mathematical expression to evaluate, e.g. '(150 - 120) / 120 * 100'"
                }
            },
            "required": ["expression"]
        }
    }
]

# Mock implementations (in interview, these would be real or provided)
MOCK_PRICES = {"AAPL": 185.50, "GOOGL": 141.20, "MSFT": 378.90, "AMZN": 178.30}
MOCK_INFO = {
    "AAPL": {"name": "Apple Inc.", "sector": "Technology", "market_cap": "2.87T"},
    "GOOGL": {"name": "Alphabet Inc.", "sector": "Technology", "market_cap": "1.76T"},
    "MSFT": {"name": "Microsoft Corp.", "sector": "Technology", "market_cap": "2.81T"},
}

def get_stock_price(ticker):
    ticker = ticker.upper()
    if ticker not in MOCK_PRICES:
        raise ValueError(f"Unknown ticker: {ticker}. Try AAPL, GOOGL, MSFT, or AMZN.")
    return json.dumps({"ticker": ticker, "price": MOCK_PRICES[ticker], "currency": "USD"})

def get_company_info(ticker):
    ticker = ticker.upper()
    if ticker not in MOCK_INFO:
        raise ValueError(f"No info available for ticker: {ticker}")
    return json.dumps(MOCK_INFO[ticker])

def calculate(expression):
    # Safety: only allow safe math operations
    allowed = set("0123456789+-*/.() ")
    if not all(c in allowed for c in expression):
        raise ValueError(f"Unsafe expression: {expression}")
    return str(eval(expression))

tool_functions = {
    "get_stock_price": get_stock_price,
    "get_company_info": get_company_info,
    "calculate": calculate,
}
```

### Step 2: Production Agent Loop with Error Handling (20 min)

```python
def run_agent(user_message, tools, tool_functions, system=None, max_turns=10):
    messages = [{"role": "user", "content": user_message}]

    for turn in range(max_turns):
        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                tools=tools,
                messages=messages,
                **({"system": system} if system else {})
            )
        except anthropic.APIError as e:
            return f"API error: {e}"

        # Handle different stop reasons
        if response.stop_reason == "end_turn":
            return "".join(b.text for b in response.content if hasattr(b, "text"))

        if response.stop_reason == "max_tokens":
            # Claude ran out of space - this is a problem
            return "Error: response exceeded max_tokens. Try a simpler query."

        if response.stop_reason != "tool_use":
            return f"Unexpected stop reason: {response.stop_reason}"

        # Add assistant response to history
        messages.append({"role": "assistant", "content": response.content})

        # Process ALL tool calls (may be parallel)
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                # Log the call
                print(f"  [{block.name}] input={json.dumps(block.input)}")

                # Execute with error handling
                try:
                    func = tool_functions.get(block.name)
                    if func is None:
                        raise ValueError(f"Unknown tool: {block.name}")
                    result = func(**block.input)
                    is_error = False
                except Exception as e:
                    result = f"Error: {str(e)}"
                    is_error = True

                print(f"  [{block.name}] {'ERROR: ' if is_error else ''}{str(result)[:100]}")

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result),
                    **({"is_error": True} if is_error else {})
                })

        messages.append({"role": "user", "content": tool_results})

    return "Max turns reached"
```

### Step 3: Test Parallel Tool Calls (15 min)

```python
# This query should trigger parallel tool calls (Claude gets both prices at once)
result = run_agent(
    "Compare the stock prices of Apple and Google. Which is more expensive?",
    tools, tool_functions,
    system="You are a financial analyst. Be concise and data-driven."
)
print(f"\nResult: {result}")

# Test error handling
result = run_agent(
    "What's the stock price of INVALID_TICKER?",
    tools, tool_functions
)
print(f"\nError case: {result}")

# Test multi-step reasoning
result = run_agent(
    "What's the percentage difference between Apple and Microsoft stock prices?",
    tools, tool_functions,
    system="You are a financial analyst. Show your work."
)
print(f"\nMulti-step: {result}")
```

### Step 4: Structured Output via tool_choice (15 min)

Use `tool_choice` to force structured JSON output without needing a real tool:

```python
# Use a "tool" to force structured output
analysis_tool = {
    "name": "format_analysis",
    "description": "Format the final analysis as structured JSON",
    "input_schema": {
        "type": "object",
        "properties": {
            "summary": {"type": "string", "description": "One-sentence summary"},
            "stocks_compared": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "ticker": {"type": "string"},
                        "price": {"type": "number"},
                        "assessment": {"type": "string"}
                    },
                    "required": ["ticker", "price", "assessment"]
                }
            },
            "recommendation": {"type": "string"}
        },
        "required": ["summary", "stocks_compared", "recommendation"]
    }
}

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    tools=[analysis_tool],
    tool_choice={"type": "tool", "name": "format_analysis"},
    messages=[{
        "role": "user",
        "content": "Compare AAPL at $185.50 and GOOGL at $141.20 for investment."
    }]
)

# Extract the structured input (this IS the output)
for block in response.content:
    if block.type == "tool_use":
        structured = block.input
        print(json.dumps(structured, indent=2))
```

### Alternative: JSON Output Config (newer approach)

```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": "Compare AAPL at $185.50 and GOOGL at $141.20 for investment."
    }],
    output_config={
        "format": {
            "type": "json_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string"},
                    "recommendation": {"type": "string"}
                },
                "required": ["summary", "recommendation"],
                "additionalProperties": False
            }
        }
    }
)
# response.content[0].text is guaranteed valid JSON matching the schema
result = json.loads(response.content[0].text)
```

---

## Drills (15 min)

1. **Error handling** - Write a tool_result with `is_error: True`. When would you use it?
2. **Parallel calls** - What does `response.content` look like when Claude calls 2 tools at once? How does your loop handle it?
3. **Structured output** - Write a request that forces JSON output using `tool_choice`. Then write one using `output_config`.

---

## Key Takeaways

- **Always handle errors gracefully** - wrap tool execution in try/except, always return a tool_result
- **`is_error: True`** tells Claude the tool failed - it can then retry or adjust
- **Parallel tool calls** - Claude may include multiple tool_use blocks in one response. Process all of them.
- **Structured output** two ways: `tool_choice` to force a tool call (input = your schema), or `output_config.format` for direct JSON
- **`strict: true`** on tool definitions guarantees schema compliance (production use)
- Handle `max_tokens` stop reason - it means Claude got cut off mid-response
