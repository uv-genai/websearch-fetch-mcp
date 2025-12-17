import asyncio
from mcp import Stdio, Client

async def test_fetch_page_md_to_local_markdown():
    # Connect to the server via stdio
    client = Client(Stdio())

    # Test fetch_page_md with an HTML page
    print("\n--- Testing fetch_page_md to markdown ---")
    fetch_md_result = await client.call_tool(
        "fetch_page_md",
        arguments={"url": "https://httpbin.org/html", "max_chars": 500}
    )
    print("fetch_page_md result:", fetch_md_result)

    # Write the markdown result to a local file
    with open("downloaded_page.md", "w") as markdown_file:
        markdown_file.write(fetch_md_result)
    print("Markdown content saved to downloaded_page.md")

if __name__ == "__main__":
    asyncio.run(test_fetch_page_md_to_local_markdown())