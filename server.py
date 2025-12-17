from fastmcp import FastMCP
import requests
import html2text
import tempfile
import os
from docling import DocumentConversionInput
from docling.document_converter import DocumentConverter

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
    # Convert HTML to markdown using docling
    with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False) as tmp:
        tmp.write(r.text)
        tmp_path = tmp.name

    input_doc = DocumentConversionInput.from_paths([tmp_path])
    converter = DocumentConverter()
    converted = converter.convert(input_doc).__next__()
    markdown_text = converted.render_as_markdown()

    os.unlink(tmp_path)
    return markdown_text[:max_chars]

if __name__ == "__main__":
    fastmcp.run()