



    Read: "Constitutional AI: Harmlessness from AI Feedback" (Anthropic Paper).

    Read: "Machines of Loving Grace" (Dario Amodei).

    Build: A simple Hello World MCP Server.

    Practice: 2-3 CodeSignal "General Coding" practice tests (focus on file/string manipulation).

    Prep: Write down the "War Story" of the hardest technical problem you solved at Roostr, specifically focusing on when the LLM failed and how you fixed it.



This is the "Founder's Trap." You have moved up the stack to orchestration and architecture, letting the AI handle the syntax implementation details.

However, **you cannot bullshit the CodeSignal assessment.** It is an automated gatekeeper. If you time out because you forgot how to open a file or sort a dictionary in pure Python without hitting `Tab`, no human will ever see your resume.

You need to undergo a **"Syntax Detox"** for the next 4–5 days. You don't need to become a LeetCode wizard, but you need to swap your "Manager/Architect" brain for your "Junior Dev" brain.

Here is the tactical plan to regain "naked coding" proficiency quickly.

### 1. The "CodeSignal" Survival Kit (Memorize This)
Anthropic’s assessment (often the "General Coding Framework") focuses on **implementation**, not algorithms. It usually involves maintaining a state, parsing strings, or managing a file system.

You must be able to write these patterns from scratch, **fast**, with zero errors.

#### A. Dictionary Manipulation (The Bread & Butter)
You will almost certainly need to group data.
```python
# Don't fumble with checking if keys exist. Use defaultdict.
from collections import defaultdict

# Grouping items
groups = defaultdict(list)
for item in data:
    groups[item['id']].append(item['val'])

# Counting items
counts = defaultdict(int)
for word in words:
    counts[word] += 1

# Sorting a dict by value (high probability task)
sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
```

#### B. String Parsing & File I/O
They often give you a "log file" or a stream of commands.
```python
# Parsing a messy string line
line = "User: Mark | Action: Login | Time: 12:00"
parts = line.split('|')
clean_parts = [p.strip().split(': ')[1] for p in parts]

# Safe casting
try:
    value = int(potential_number)
except ValueError:
    value = 0
```

#### C. The Custom Class (State Management)
Question 4 is usually "Build a filesystem" or "Build a bank." You need to be comfortable writing a class with state immediately.
```python
class System:
    def __init__(self):
        self.database = {} # id -> data
    
    def process_command(self, command, args):
        # Dispatcher pattern - memorize this structure
        if command == "CREATE":
            return self._create(args)
        elif command == "DELETE":
            return self._delete(args)
            
    def _create(self, args):
        # logic here
        return "success"
```

### 2. The "MCP" Strategy: Don't Memorize Boilerplate, Memorize Pydantic
You mentioned the MCP server. In a live interview, they won't ask you to write the JSON-RPC transport layer from memory. They *will* ask you to write the **tool logic**.

Anthropic (and modern Python engineering) relies heavily on **Pydantic**. If you can write Pydantic models fluently without AI, you look like a pro.

**Practice writing this completely manually:**

```python
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional

# Define the structure of the data you expect from the customer
class CustomerQuery(BaseModel):
    query: str
    filters: Optional[List[str]] = Field(default_factory=list)
    limit: int = Field(default=10, ge=1, le=100) # Validation logic built-in

# Simulate the tool logic
def search_tool(json_input: str):
    try:
        # Validate input (Anthropic loves this safety check)
        params = CustomerQuery.model_validate_json(json_input)
        
        # Actual logic
        print(f"Searching for {params.query}")
        
    except ValidationError as e:
        return f"Error: {e}"
```
*Why this matters:* It shows you care about **types** and **validation** (Safety), not just hacking scripts together.

### 3. The 3-Day Detox Plan

You need to force your brain to retrieve syntax it hasn't accessed in years.

**Day 1: The "No-Copilot" Hell**
*   Turn off Github Copilot/Cursor/ChatGPT.
*   Go to **CodeSignal's Practice Area** (specifically "Arcade" -> "Intro").
*   Solve 5 easy problems.
*   *Observation:* You will feel frustrated. You will forget if it's `len(arr)` or `arr.length`. You will syntax error on `enumerate`. **This is the point.** You need to flush this out now, not during the test.

**Day 2: The "File System" Drill**
*   Anthropic loves "file system" or "in-memory database" problems.
*   **Task:** Open a blank text editor (Notepad or TextEdit).
*   **Prompt:** "Write a Python script that accepts a list of strings representing file paths (e.g., `/usr/bin/java`) and builds a nested dictionary representing the directory structure."
*   Do it without running it until the end. Then debug.

**Day 3: The Mock MCP**
*   Build that MCP server I mentioned, but do it this way:
    1.  Read the docs for 10 minutes.
    2.  Close the docs.
    3.  Open VS Code with **Copilot disabled**.
    4.  Try to implement a basic "Echo" server.
    5.  When you get stuck on syntax, **search Google/StackOverflow**, DO NOT ask Claude.
    *   *Why:* Searching SO reinforces the neural pathway of "finding the answer" vs "being fed the answer."

### 4. How to handle it if you blank out in the interview

If you are in the live coding round and you forget the syntax for something (e.g., how to sort a list of dictionaries by two keys):

**DO NOT:** "Uh, I usually let Copilot do this..." (looks weak).
**DO:** "I'm blanking on the exact syntax for the lambda sort, but the logic is to sort by X then Y. I'm going to write a helper function or look up the reference quickly."

**The Founding FDE specific defense:**
Since you are applying for a *founding* role, your value is architecture + speed. If you get stuck on syntax, zoom out:
*"I haven't written this specific sorting boilerplates by hand in a while because I've been focused on the agent architecture, but here is the pseudocode logic which is correct..."*

**TL;DR:** Spend 4 hours this weekend on **CodeSignal practice mode** with all AI turned off. It will be painful, but it will pass the Recruiter/OA gate.