"""Portable MCP branding; the account app keeps its original identity."""
import base64
from pathlib import Path
from mcp_types import Icon


def icons():
    data = Path(__file__).with_name("assets").joinpath("icon.svg").read_bytes()
    return [Icon(src="data:image/svg+xml;base64," + base64.b64encode(data).decode(),
                 mime_type="image/svg+xml", sizes=["512x512"])]
