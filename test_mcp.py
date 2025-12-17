import asyncio
from mcp import Stdio, Client

async def main():
    # Connect to the server via stdio
    client = Client(Stdio())
    
    # List available tool names
    tool_names = await client.list_tool_names()
    print("Available tools:", tool_names)
    
    # Test search_web
    print("\n--- Testing search_web ---")
    search_result = await client.call_tool(
        "search_web",
        arguments={"query": "test", "max_chars": 100, "num_results": 1}
    )
    print("search_web result:", search_result)
    
    # Test fetch_page
    print("\n--- Testing fetch_page ---")
    fetch_result = await client.call_tool(
        "fetch_page",
        arguments={"url": "https://httpbin.org/html", "max_chars": 100}
    )
    print("fetch_page result:", fetch_result)
    
    # Test fetch_page_md
    print("\n--- Testing fetch_page_md ---")
    fetch_md_result = await client.call_tool(
        "fetch_page_md",
        arguments={"url": "https://httpbin.org/html", "max_chars": 100}
    )
    print("fetch_page_md result:", fetch_md_result)

if __name__ == "__main__":
    asyncio.run(main())