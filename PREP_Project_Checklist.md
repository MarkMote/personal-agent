DO: 
- Make Python Cheatsheet with anything i need to look up.
- Review: https://interviewing.io/anthropic-interview-questions#question-design
- **CodeSignal General Coding Framework** - [Official Guide](https://support.codesignal.com/hc/en-us/articles/360040703634-General-Coding-Framework-Framework-Structure) - Defines the rules, scoring, and IDE constraints for the 70-minute automated assessment.
* **Model Context Protocol (MCP)** - [Official Docs](https://modelcontextprotocol.io/introduction) - Documentation for the open standard FDEs use to connect Claude to data.
* **Anthropic Research** - [Constitutional AI Paper](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) - The foundational paper explaining their specific approach to safety and alignment.
* **Dario Amodei (CEO)** - [Machines of Loving Grace](https://darioamodei.com/machines-of-loving-grace) - Mandatory cultural reading on the company's optimistic long-term vision.
* **Eugene Yan** - [Patterns for Building LLM Systems](https://eugeneyan.com/writing/llm-patterns/) - High-level architecture guide for production LLMs (Evals, RAG, Guardrails).
* **Interviewing.io** - [Anthropic Interview Guide](https://interviewing.io/guides/anthropic-software-engineer-interview) - Detailed breakdown of the interview loop and historically reported questions.
* **Anthropic Console** - [Prompt Engineering Interactive Tutorial](https://console.anthropic.com/dashboard) - Their official "right way" to prompt (requires login).
* **Applied LLM Reading** - [Chip Huyen's "Building LLM Applications for Production"](https://huyenchip.com/2023/04/11/llm-engineering.html) - The industry standard reference for the messy reality of FDE work.



Here is the comprehensive list of every project archetype you need to master for the Anthropic FDE process, separated by interview stage.

### **Round 1: CodeSignal (The General Coding Framework)**
*Focus: Python Standard Library, Data Structures, Speed.*

#### **Project 1: The In-Memory File System**
*   **The Prompt:** Build a class `FileSystem` with `mkdir(path)`, `add_content(path, str)`, `ls(path)`.
*   **Success Criteria:** Can you handle nested paths like `/a/b/c` using a recursive dictionary structure in <15 mins?
*   **Practice Link:** [LeetCode 588 (Premium) - Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/)
    *   *Free Alternative:* [LeetCode 1166 - Design File System](https://leetcode.com/problems/design-file-system/)

#### **Project 2: The Transactional Database (Key-Value Store)**
*   **The Prompt:** Build a `KVStore` with `set(k, v)`, `get(k)`, `begin()`, `commit()`, `rollback()`.
*   **Success Criteria:** Can you implement nested transactions (stack of state deltas) where a rollback only undoes the most recent `begin()`?
*   **Practice Link:** [LeetCode 677 - Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/) (Basic KV)
    *   *Logic Helper:* [LeetCode 1146 - Snapshot Array](https://leetcode.com/problems/snapshot-array/) (Version history logic)

#### **Project 3: The Load Balancer / Rate Limiter**
*   **The Prompt:** Build a `RequestManager` that assigns tasks to servers based on load, or limits requests (e.g., "Max 3 requests per 10 seconds").
*   **Success Criteria:** Can you use `heapq` to find the minimum load server efficiently, or `deque` to clean up old timestamps for rate limiting?
*   **Practice Link:** [LeetCode 359 - Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/)
    *   *Advanced:* [LeetCode 362 - Design Hit Counter](https://leetcode.com/problems/design-hit-counter/)

#### **Project 4: The Spreadsheet (Dependency Graph)**
*   **The Prompt:** Build a `Sheet` where cell A1 can depend on B2. `set_cell(id, val)`, `get_cell(id)`. Detect cycles.
*   **Success Criteria:** Can you perform a topological sort or DFS to detect "A->B->A" cycles before applying an update?
*   **Practice Link:** [LeetCode 210 - Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) (This is the underlying logic for dependencies)

#### **Project 5: The Game Grid (2D Array Logic)**
*   **The Prompt:** Implement a game board (Tetris, Candy Crush, Othello). "Drop a piece at col X, clear rows if full."
*   **Success Criteria:** Can you iterate a matrix backwards (`range(n-1, -1, -1)`) to apply gravity without index errors?
*   **Practice Link:** [LeetCode 289 - Game of Life](https://leetcode.com/problems/game-of-life/) (State updates)
    *   *Specific Logic:* [LeetCode 723 - Candy Crush](https://leetcode.com/problems/candy-crush/) (Premium)

#### **Project 6: The Log Aggregator (String Parsing)**
*   **The Prompt:** Parse raw log strings `"id=1|time=100"`. Filter by time window. Group by ID.
*   **Success Criteria:** Can you parse strings and sort a list of dictionaries by multiple keys (e.g., Time desc, ID asc) using `lambda`?
*   **Practice Link:** [LeetCode 1169 - Invalid Transactions](https://leetcode.com/problems/invalid-transactions/) (String parsing + Logic)

---

### **Round 2 & 3: FDE / Onsite Specifics**
*Focus: Implementation of Agentic Systems from scratch (FastAPI, Pydantic, Manual HTTP).*

#### **Project 7: The Manual MCP Server**
*   **The Prompt:** Write a Model Context Protocol server that exposes a local SQLite DB to Claude.
*   **Success Criteria:** Can you write the Pydantic models for the tool schema and the request handler without looking at the docs?
*   **Practice Link:** [Anthropic MCP Quickstart](https://modelcontextprotocol.io/quickstart) (Build the "SQLite" example manually).

#### **Project 8: The "ReAct" Agent Loop**
*   **The Prompt:** Write a function `run_agent(query)` that loops: Call LLM -> Parse JSON Tool Call -> Exec Function -> Feed Result Back.
*   **Success Criteria:** Can you manually parse the LLM's output string into JSON and handle `json.JSONDecodeError` gracefully?
*   **Practice Link:** [LangChain "ReAct" Concept](https://react-lm.github.io/) (Read the logic, then code it in raw Python).

#### **Project 9: The Async Background Job**
*   **The Prompt:** Build a FastAPI endpoint `POST /analyze` that accepts a document and processes it in the background without blocking the return.
*   **Success Criteria:** Correct use of `async def`, `await`, and `BackgroundTasks` in FastAPI.
*   **Practice Link:** [FastAPI Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) (Re-create the tutorial code from memory).

#### **Project 10: The Streaming Response Generator**
*   **The Prompt:** Write a generator function that yields chunks of tokens simulating an LLM stream, and an API endpoint that streams this to the client.
*   **Success Criteria:** Use of `yield` and `StreamingResponse` class.
*   **Practice Link:** [FastAPI Response Streaming](https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse)