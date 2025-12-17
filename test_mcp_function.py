import asyncio
# Import the function directly; the __main__ block won't run on import
from server import fetch_page_md

async def main():
    # Test converting a simple HTML page to markdown
    result = await fetch_page_md("https://httpbin.org/html", max_chars=200)
    print("Markdown result:")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())