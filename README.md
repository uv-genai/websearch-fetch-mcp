# WebSearch-Fetch MCP Server

An MCP server that provides web search and page fetch capabilities for coding agents.

## Tools

- `search_web(query: str, max_chars: int = 200, num_results: int = 1)` - Perform a web search using DuckDuckGo and return up to `num_results` snippets, combined and limited to `max_chars` characters.
- `fetch_page(url: str, max_chars: int = 2000)` - Fetch the content of a single web page and return it as plain text, limited to `max_chars` characters.
- `fetch_page_md(url: str, max_chars: int = 2000)` - Fetch a web page and return its content converted to markdown, limited to `max_chars` characters.

## Usage

See the [MCP documentation](https://github.com/modelcontextprotocol) for details on integrating this server with agents.

## License

MIT