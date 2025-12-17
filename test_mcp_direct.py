import asyncio
from server import fetch_page_md

async def main():
    result = await fetch_page_md("https://example.com", max_chars=200)
    print("Markdown result:", result[:200])

if __name__ == "__main__":
    asyncio.run(main())