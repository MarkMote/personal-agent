# Day 7: MCP (Model Context Protocol) (~2 hrs)

**Goal:** Understand MCP conceptually and build a working MCP server. This probably won't be the interview task, but knowing MCP shows you understand Anthropic's ecosystem vision.

---

## Reading (30 min)

1. **MCP Overview** - https://modelcontextprotocol.io/introduction
   - MCP = standardized protocol for connecting AI models to external data/tools
   - "USB-C for AI" - one protocol, many integrations
   - Three primitives: **Tools** (callable functions), **Resources** (readable data), **Prompts** (reusable templates)
   - Transport: stdio JSON-RPC (local) or HTTP SSE (remote)

2. **MCP Connector** (API-side) - https://platform.claude.com/docs/en/agents-and-tools/mcp-connector
   - Connect to MCP servers directly from the Messages API
   - `mcp_servers` array in the request + `mcp_toolset` in tools
   - Beta header: `mcp-client-2025-11-20`

3. **MCP Skilljar Course** (skim) - https://anthropic.skilljar.com/introduction-to-model-context-protocol

**Key concepts:**
- MCP servers expose tools and resources via JSON-RPC
- Clients (like Claude) connect and discover available tools
- The protocol defines: `initialize`, `tools/list`, `tools/call`, `resources/list`, `resources/read`
- Servers run as separate processes; communication via stdin/stdout or HTTP

---

## Project A: Hello-World MCP Server (45 min)

From Problem 10 in the practice set. Build a minimal MCP server.

### Step 1: Understand the Protocol (10 min)

MCP uses JSON-RPC 2.0. Messages look like:

```json
// Request
{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}

// Response
{"jsonrpc": "2.0", "id": 1, "result": {...}}

// Notification (no id, no response expected)
{"jsonrpc": "2.0", "method": "notifications/initialized"}
```

### Step 2: Build the Server (25 min)

```python
#!/usr/bin/env python3
"""Minimal MCP server that exposes a 'hello' tool."""
import json
import sys

PROTOCOL_VERSION = "2024-11-05"
SERVER_INFO = {"name": "hello-mcp", "version": "0.1.0"}

TOOLS = [{
    "name": "hello",
    "description": "Say hello to someone by name",
    "inputSchema": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "Name of person to greet"}
        },
        "required": ["name"]
    }
}]

def send(msg: dict) -> None:
    """Send a JSON-RPC message to stdout."""
    data = json.dumps(msg, separators=(',', ':'))
    sys.stdout.write(data + '\n')
    sys.stdout.flush()

def handle_request(req: dict) -> None:
    method = req.get("method", "")
    req_id = req.get("id")

    # Notifications have no id - don't respond
    if req_id is None:
        sys.stderr.write(f"Notification: {method}\n")
        return

    if method == "initialize":
        send({
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {}},
                "serverInfo": SERVER_INFO
            }
        })

    elif method == "tools/list":
        send({
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"tools": TOOLS}
        })

    elif method == "tools/call":
        tool_name = req["params"].get("name")
        arguments = req["params"].get("arguments", {})

        if tool_name == "hello":
            name = arguments.get("name", "World")
            send({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": f"Hello, {name}!"}]
                }
            })
        else:
            send({
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Unknown tool: {tool_name}"
                }
            })

    else:
        send({
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32601,
                "message": f"Unknown method: {method}"
            }
        })

def main():
    sys.stderr.write("MCP Hello server starting...\n")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            sys.stderr.write(f"Received: {req.get('method', 'unknown')}\n")
            handle_request(req)
        except json.JSONDecodeError as e:
            sys.stderr.write(f"Bad JSON: {e}\n")
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")

if __name__ == "__main__":
    main()
```

### Step 3: Test It (10 min)

```bash
# Test manually by piping JSON
echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' | python mcp_hello.py
echo '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}' | python mcp_hello.py
echo '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"hello","arguments":{"name":"Mark"}}}' | python mcp_hello.py
```

Or test with the MCP Inspector:
```bash
npx @modelcontextprotocol/inspector python mcp_hello.py
```

---

## Project B: MCP-over-SQLite Server (45 min)

Extend the MCP server to expose database tools. From Problem 13.

```python
#!/usr/bin/env python3
"""MCP server backed by SQLite."""
import json, sys, sqlite3, csv, io

DB_FILE = "mcp.db"

def send(msg):
    sys.stdout.write(json.dumps(msg, separators=(',', ':')) + '\n')
    sys.stdout.flush()

class SQLiteMCPServer:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, isolation_level=None)
        self.conn.row_factory = sqlite3.Row

    def handle(self, req):
        method = req.get("method", "")
        req_id = req.get("id")

        if req_id is None:
            return  # notification

        try:
            if method == "initialize":
                self._initialize(req_id)
            elif method == "tools/list":
                self._tools_list(req_id)
            elif method == "tools/call":
                self._tools_call(req_id, req.get("params", {}))
            elif method == "resources/list":
                self._resources_list(req_id)
            elif method == "resources/read":
                self._resources_read(req_id, req.get("params", {}))
            else:
                send({"jsonrpc": "2.0", "id": req_id,
                      "error": {"code": -32601, "message": f"Unknown: {method}"}})
        except Exception as e:
            send({"jsonrpc": "2.0", "id": req_id,
                  "error": {"code": -32001, "message": str(e)}})

    def _initialize(self, req_id):
        send({"jsonrpc": "2.0", "id": req_id, "result": {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {}, "resources": {}},
            "serverInfo": {"name": "sqlite-mcp", "version": "0.1.0"}
        }})

    def _tools_list(self, req_id):
        tools = [
            {
                "name": "list_tables",
                "description": "List all tables in the database with row counts",
                "inputSchema": {"type": "object", "properties": {}}
            },
            {
                "name": "run_sql",
                "description": "Execute a SQL query and return results (paginated)",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "page": {"type": "integer", "default": 1},
                        "page_size": {"type": "integer", "default": 100}
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "create_table",
                "description": "Create a new table with the given SQL schema",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "schema": {"type": "string"}
                    },
                    "required": ["name", "schema"]
                }
            }
        ]
        send({"jsonrpc": "2.0", "id": req_id, "result": {"tools": tools}})

    def _tools_call(self, req_id, params):
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "list_tables":
            cursor = self.conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )
            tables = []
            for row in cursor:
                count = self.conn.execute(
                    f"SELECT COUNT(*) FROM [{row['name']}]"
                ).fetchone()[0]
                tables.append({"name": row["name"], "row_count": count})
            result = json.dumps(tables)

        elif name == "run_sql":
            query = args["query"]
            page = min(max(args.get("page", 1), 1), 1000)
            page_size = min(max(args.get("page_size", 100), 1), 500)

            # Get total count (approximate)
            cursor = self.conn.execute(query)
            all_rows = cursor.fetchall()
            total = len(all_rows)
            columns = [d[0] for d in cursor.description] if cursor.description else []

            # Paginate
            start = (page - 1) * page_size
            page_rows = [dict(r) for r in all_rows[start:start + page_size]]

            result = json.dumps({
                "columns": columns, "rows": page_rows,
                "total": total, "page": page, "page_size": page_size
            })

        elif name == "create_table":
            self.conn.execute(f"CREATE TABLE [{args['name']}] ({args['schema']})")
            result = json.dumps({"ok": True})

        else:
            send({"jsonrpc": "2.0", "id": req_id,
                  "error": {"code": -32601, "message": f"Unknown tool: {name}"}})
            return

        send({"jsonrpc": "2.0", "id": req_id,
              "result": {"content": [{"type": "text", "text": result}]}})

    def _resources_list(self, req_id):
        cursor = self.conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )
        resources = [{
            "uri": f"sqlite:///{row['name']}.csv",
            "name": f"{row['name']} (CSV)",
            "mimeType": "text/csv"
        } for row in cursor]
        send({"jsonrpc": "2.0", "id": req_id, "result": {"resources": resources}})

    def _resources_read(self, req_id, params):
        uri = params.get("uri", "")
        table = uri.replace("sqlite:///", "").replace(".csv", "")

        cursor = self.conn.execute(f"SELECT * FROM [{table}] LIMIT 1000")
        columns = [d[0] for d in cursor.description]

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(columns)
        for row in cursor:
            writer.writerow(row)

        send({"jsonrpc": "2.0", "id": req_id, "result": {
            "contents": [{"uri": uri, "mimeType": "text/csv", "text": output.getvalue()}]
        }})

def main():
    server = SQLiteMCPServer(DB_FILE)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            server.handle(json.loads(line))
        except json.JSONDecodeError:
            pass

if __name__ == "__main__":
    main()
```

---

## Using MCP from the API (Know This, Don't Build It)

```python
# How to connect to an MCP server from the Messages API
response = client.beta.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    mcp_servers=[{
        "type": "url",
        "url": "https://example-mcp.com/sse",
        "name": "my-mcp",
        "authorization_token": "TOKEN"
    }],
    tools=[{
        "type": "mcp_toolset",
        "mcp_server_name": "my-mcp"
    }],
    messages=[{"role": "user", "content": "What tools do you have?"}],
    betas=["mcp-client-2025-11-20"]
)
```

---

## Key Takeaways

- MCP = standardized protocol for AI <-> tools/data. JSON-RPC over stdio or HTTP.
- Three primitives: **Tools** (functions), **Resources** (data), **Prompts** (templates)
- Server implements: `initialize`, `tools/list`, `tools/call`, optionally `resources/list`, `resources/read`
- From the API: use `mcp_servers` + `mcp_toolset` to connect to remote MCP servers
- In the interview: if asked about MCP, explain the architecture. Building one from scratch is a 45-min exercise.
- **Cultural point:** MCP represents Anthropic's vision of open, standardized AI integration
