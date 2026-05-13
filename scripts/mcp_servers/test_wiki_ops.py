import pytest
import sys
import os

# Add root to sys.path for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def test_mcp_initialization():
    from scripts.mcp_servers.wiki_ops import mcp
    assert mcp.name == "Wiki-Ops-MCP"

def test_query_wiki():
    from scripts.mcp_servers.wiki_ops import query_wiki
    result = query_wiki("test")
    assert "Mock" in result
