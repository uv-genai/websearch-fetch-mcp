# AGENTS.md – Working Guide for the WebSearch-Fetch MCP Server

## Overview
This repository contains an MCP (Model Context Protocol) server implementing web search and page fetch capabilities. It is intended for use with AI agents that need to retrieve web content as part of their reasoning or planning processes.

## Essential Commands

| Command | Description | Example |
|---------|-------------|---------|
| `python server.py` | Starts the MCP server. The server exposes three tools: `search_web`, `fetch_page`, and `fetch_page_md`. | `python server.py` |
| `python -m pip install -r requirements.txt` | Installs the Python dependencies required to run the server and tests. | `python -m pip install -r requirements.txt` |
| `python -m pytest` (or `pytest`) | Runs the test suite located in `test_*.py` files. Tests verify the behavior of `search_web`, `fetch_page`, and `fetch_page_md` via the FastMCP client. | `pytest` |
| `python test_mcp.py` | Direct execution of the sample test script which demonstrates client usage. | `python test_mcp.py` |
| `python -c "import fastmcp; print(fastmcp.__version__)"` | Confirms the FastMCP library version in use. | `python -c "import fastmcp; print(fastmcp.__version__)"` |

> **Note:** There is no dedicated build or deployment pipeline in this minimal repository. All operations are performed directly via Python execution or standard shell commands.

## Code Organization

- `server.py`: Core implementation of the MCP server. Defines the FastMCP instance and registers three async tools:
  - `search_web(query: str, max_chars: int = 200, num_results: int = 1)`
  - `fetch_page(url: str, max_chars: int = 2000)`
  - `fetch_page_md(url: str, max_chars: int = 2000)`
- `test_*.py`: Test scripts that instantiate a FastMCP client using stdio transport and call the registered tools to validate functionality.
- `requirements.txt`: Lists runtime dependencies (`mcp[server]`, `requests`, `html2text`, `markdownify`).

The repository follows a flat structure with all source code in the root directory. There are no additional sub‑packages or configuration files (e.g., `setup.py`, `Makefile`).

## Naming Conventions & Style Patterns

- **Functions & Variables**: Use `snake_case` naming (e.g., `search_web`, `fetch_page_md`).
- **Tool Registration**: Each tool is decorated with `@fastmcp.tool()` and is an `async def` function returning a `str`.
- **Error Handling**: Functions perform basic validation (e.g., HTTP status check) and return descriptive error messages as strings.
- **Documentation**: Minimal inline comments are used; full documentation is provided in the README and docstrings.

## Testing Approach & Patterns

1. **Client Connection**: Tests use `fastmcp=Client(Stdio())` to connect to the server over stdio.
2. **Tool Invocation**: Tools are called via `client.call_tool(name, arguments={...})`.
3. **Async Flow**: Tests are `async def main()` and run with `asyncio.run(main())`.
4. **Verification**: Results are printed to stdout; assertions are left to the test runner.

### Running Tests

- Ensure dependencies are installed.
- Execute `pytest` or `python -m pytest` from the repository root.
- Test output appears in the console; failures indicate mismatches between expected and actual tool responses.

## Important Gotchas & Non‑Obvious Patterns

- **STDIO Transport**: The server expects to be launched as a separate process and communicates via standard input/output. Agents must spawn the process and manage its lifecycle.
- **Async Context**: All exposed tools are asynchronous; forgetting to `await` will result in unresolved coroutine errors.
- **Rate Limits**: `search_web` performs HTTP requests to DuckDuckGo. Excessive calls may trigger temporary bans; implement exponential back‑off if integrating in a long‑running agent.
- **HTML Parsing Fragility**: `search_web` parses HTML using a regular expression (`<div class="result">(.*?)</div>`). Changes to DuckDuckGo’s page structure can break the parser silently.
- **Environment Isolation**: The repository uses a virtual environment (`.venv`). Activate it (`source .venv/bin/activate`) when installing or testing locally to avoid polluting the global Python environment.
- **No Auto‑Reload**: The server does not watch for code changes. Restart the process to pick up modifications.

## Project‑Specific Context

- **No CI/CD Configuration**: The repo does not include GitHub Actions, GitLab CI, or other CI configurations. Build and test steps must be executed manually.
- **No Code‑style Enforcement**: There is no `.editorconfig`, `pre‑commit`, or linter configuration committed. Teams may adopt personal preferences (e.g., `black`, `flake8`) but they are not required.
- **License**: MIT – free to use, modify, and distribute in both open‑source and commercial contexts.

## Adding New Agents or Extending Functionality

1. **Create a New Tool**  
   - Add an `async def new_tool(...)` function in `server.py`.  
   - Decorate with `@fastmcp.tool()`.  
   - Document the purpose, parameters, and return value in the function docstring.  

2. **Update Tests**  
   - Add a corresponding test case in a new `test_*.py` file or extend an existing test.  
   - Follow the same async pattern and tool‑calling syntax.  

3. **Documentation**  
   - Extend the README with usage examples for the new tool.  
   - Update this `AGENTS.md` if new commands or patterns emerge (e.g., additional dependencies).  

## Summary

- **Run**: `python server.py`  
- **Install**: `python -m pip install -r requirements.txt`  
- **Test**: `pytest` or `python -m pytest`  
- **Code Pattern**: `@fastmcp.tool()` + `async def` + `client.call_tool`  
- **Gotchas**: async handling, stdio transport, rate limiting, HTML parsing fragility  

Keep this document up‑to‑date as the project evolves. Future contributors should review it before adding new features or modifying existing tools.