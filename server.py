from fastmcp import FastMCP
import requests
import html2text
from markdownify import markdownify

fastmcp = FastMCP("websearch-fetch-mcp")

@fastmcp.tool()
async def search_web(query: str, max_chars: int = 200, num_results: int = 1) -> str:
    r = requests.get("https://duckduckgo.com/html/", params={"q": query})
    import re
    snippets = re.findall(r'<div class="result">(.*?)</div>', r.text)
    selected = snippets[:num_results]
    combined = "\n\n".join(selected)
    return combined[:max_chars]

@fastmcp.tool()
async def fetch_page(url: str, max_chars: int = 2000) -> str:
    r = requests.get(url)
    if r.status_code != 200:
        return "Failed to fetch"
    text = html2text.html2text(r.text)
    return text[:max_chars]

@fastmcp.tool()
async def fetch_page_md(url: str, max_chars: int = 2000) -> str:
    r = requests.get(url)
    if r.status_code != 200:
        return "Failed to fetch"
    text = markdownify(r.text, heading_style="ATX")
    return text[:max_chars]

if __name__ == "__main__":
    fastmcp.run()