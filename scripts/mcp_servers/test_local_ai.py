import pytest
import sys
import os

# Add root to sys.path for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def test_mcp_ai_initialization():
    from scripts.mcp_servers.local_ai import mcp
    assert mcp.name == "Local-AI-MCP"

def test_gap_check():
    from scripts.mcp_servers.local_ai import gap_check
    result = gap_check("test atom")
    assert "WARNING" in result or "Mock" in result
