-------------------------------------------------
Problem 23. LangChain Fundamentals – Build, Then Remove It
-------------------------------------------------
This project walks you through **building the same application three times**:
1. **Part A**: With LangChain (to learn the abstractions)
2. **Part B**: Without LangChain (to understand what it abstracts)
3. **Part C**: Critical analysis (to articulate trade-offs)

You'll build a **travel assistant** that:
- Answers questions using tools (weather, flights, hotels)
- Remembers conversation history
- Retrieves from a knowledge base (RAG)

---

## Part A: With LangChain (3 sub-tasks)

### A1. Simple Chain + Prompt Template
**File**: `lc_chain.py`

Build a Q&A chain that:
- Uses `ChatOpenAI` (or `ChatAnthropic`)
- Takes a city name as input
- Uses `PromptTemplate` to format: `"Tell me 3 fun facts about {city}"`
- Returns the LLM response

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# TODO: implement
def create_fact_chain() -> LLMChain:
    ...

if __name__ == "__main__":
    chain = create_fact_chain()
    result = chain.invoke({"city": "Tokyo"})
    print(result)
```

**Constraints**:
- Keep it ≤ 30 lines
- Must use `PromptTemplate` (not f-strings)
- Print the actual prompt sent to the LLM

---

### A2. ReAct Agent with Tools
**File**: `lc_agent.py`

Build an agent with 3 tools:
1. `get_weather(city: str) -> str` – mock returns "Sunny, 72°F"
2. `search_flights(origin: str, dest: str) -> str` – mock returns "3 flights available"
3. `get_hotel(city: str) -> str` – mock returns "Best Western, $120/night"

Use:
- `@tool` decorator to define tools
- `create_react_agent` + `AgentExecutor`
- `ChatMessageHistory` for memory

Test query: *"I want to visit Paris. What's the weather and find me a hotel."*

```python
from langchain.agents import create_react_agent, AgentExecutor, tool
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    return f"Sunny, 72°F in {city}"

# TODO: add 2 more tools, build agent, test
```

**Constraints**:
- Agent must call 2+ tools in one invocation
- Print intermediate steps (tool calls)
- Keep ≤ 80 lines

---

### A3. RAG Pipeline
**File**: `lc_rag.py`

Build a RAG system over 5 travel documents:
- "Paris is known for the Eiffel Tower..."
- "Tokyo has the best sushi..."
- (3 more short docs about cities)

Use:
- `CharacterTextSplitter` (chunk_size=100)
- `OpenAIEmbeddings` (or `HuggingFaceEmbeddings`)
- `FAISS` vector store
- `RetrievalQA` chain

Test query: *"What is Paris known for?"*

```python
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

docs = [
    "Paris is known for the Eiffel Tower and croissants.",
    # TODO: add 4 more
]

# TODO: build RAG pipeline
```

**Constraints**:
- Must return source documents with answer
- Keep ≤ 60 lines
- Print retrieved chunks before answer

---

## Part B: Without LangChain (re-implement)

### B1. Chain without LangChain
**File**: `raw_chain.py`

Re-implement A1 using **only** OpenAI SDK (or Anthropic SDK).

```python
from openai import OpenAI

client = OpenAI()

def get_facts(city: str) -> str:
    prompt = f"Tell me 3 fun facts about {city}"
    # TODO: call client.chat.completions.create
    ...

if __name__ == "__main__":
    print(get_facts("Tokyo"))
```

**Compare**:
- Line count: LangChain vs raw
- Clarity: which is easier to debug?

---

### B2. Agent without LangChain
**File**: `raw_agent.py`

Re-implement A2 using:
- OpenAI function calling (or Anthropic tool use)
- Manual loop: LLM → parse tool call → execute → feed back → repeat

```python
import json
from openai import OpenAI

client = OpenAI()

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather for a city",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"]
            }
        }
    },
    # TODO: add 2 more
]

def execute_tool(name: str, args: dict) -> str:
    # TODO: dispatch to actual functions
    ...

def run_agent(query: str, max_steps: int = 5) -> str:
    messages = [{"role": "user", "content": query}]
    # TODO: implement loop
    ...

if __name__ == "__main__":
    print(run_agent("I want to visit Paris. What's the weather?"))
```

**Compare**:
- Token efficiency (LangChain adds overhead in prompts)
- Error handling (who owns retry logic?)
- Debuggability (print intermediate JSON)

---

### B3. RAG without LangChain
**File**: `raw_rag.py`

Re-implement A3 using:
- `sentence-transformers` for embeddings
- `faiss-cpu` for vector store
- Raw OpenAI chat completion

```python
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from openai import OpenAI

model = SentenceTransformer('all-MiniLM-L6-v2')
client = OpenAI()

docs = [...]  # same 5 docs

# TODO: embed, build FAISS index, retrieve, generate answer
```

**Compare**:
- Dependency count
- Flexibility (can you swap retriever logic?)
- Performance (measure embedding time)

---

## Part C: Critical Analysis

**File**: `ANALYSIS.md`

Answer these questions (200–400 words each):

1. **What LangChain abstracts**  
   List 5 things LangChain handles that you had to write manually in Part B.

2. **When LangChain helps**  
   Give 2 scenarios where LangChain accelerates development.

3. **When LangChain hurts**  
   Give 2 scenarios where raw code is better (cite your experience from Part B).

4. **Memory comparison**  
   - LangChain: `ConversationBufferMemory` vs `ConversationSummaryMemory`
   - Raw: how would you implement each? (pseudo-code)

5. **Why people remove it in production**  
   List 3 common complaints (e.g., token overhead, black-box debugging, version churn).

6. **Your recommendation**  
   When would you use LangChain vs raw Python in a production system?

---

## Deliverables Checklist

- [ ] `lc_chain.py` – working chain with prompt template
- [ ] `lc_agent.py` – ReAct agent calling 3 tools
- [ ] `lc_rag.py` – RAG pipeline with source citations
- [ ] `raw_chain.py` – same as lc_chain without LangChain
- [ ] `raw_agent.py` – same as lc_agent without LangChain
- [ ] `raw_rag.py` – same as lc_rag without LangChain
- [ ] `ANALYSIS.md` – answers to 6 questions
- [ ] `requirements.txt` – all dependencies
- [ ] `README.md` – how to run each file

---

## Constraints

- Use **Python 3.9+**
- Total project ≤ 500 lines (excluding analysis)
- All scripts must be **runnable** (mock API keys if needed)
- Include **print statements** showing intermediate steps
- Document **token counts** for Part A vs Part B (at least for agent)

---

## Bonus Challenges (optional)

1. Add **streaming** to the agent (Part A and B)
2. Implement **ConversationSummaryMemory** from scratch (Part B)
3. Add **retry logic** with exponential backoff (Part B)
4. Benchmark **latency**: LangChain vs raw (include results in analysis)
5. Show a **breaking change** in LangChain (pick a version bump, show deprecated API)