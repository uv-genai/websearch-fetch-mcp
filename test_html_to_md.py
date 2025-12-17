import pytest
from docling.document_converter import DocumentConverter, InputFormat
from docling.document_converter import DocumentStream
from io import BytesIO

def test_html_to_markdown_conversion():
    html = "<html><body><h1>Title</h1><p>Hello</p></body></html>"
    markdown = (
        DocumentConverter(allowed_formats=[InputFormat.HTML])
        .convert(DocumentStream(name="", stream=BytesIO(html.encode())))
        .document
        .export_to_markdown()
    )
    # Basic sanity checks
    assert "# Title" in markdown
    assert "Hello" in markdown
    # No raw HTML tags should remain
    assert "<" not in markdown

