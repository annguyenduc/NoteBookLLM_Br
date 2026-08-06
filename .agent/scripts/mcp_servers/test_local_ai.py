import pytest
import sys
import os
import importlib.util

# Add root to sys.path for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))


def load_gap_check_module():
    module_path = os.path.join(ROOT_DIR, ".agent", "skills", "wiki-ingest", "scripts", "gap_check.py")
    spec = importlib.util.spec_from_file_location("gap_check_script", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_mcp_ai_initialization():
    from scripts.mcp_servers.local_ai import mcp
    assert mcp.name == "Local-AI-MCP"

def test_gap_check_uses_ollama_response_and_writes_review_artifact(monkeypatch, tmp_path):
    from scripts.mcp_servers import local_ai

    calls = []

    def fake_ollama_chat(prompt, model="gemma3:4b"):
        calls.append((prompt, model))
        return "- [Concept] Test Gap: Useful candidate."

    monkeypatch.setattr(local_ai, "ollama_chat", fake_ollama_chat)
    monkeypatch.setenv("LOCAL_AI_REVIEW_ROOT", str(tmp_path))
    result = local_ai.gap_check("test atom")

    assert "review_artifact:" in result
    assert "- [Concept] Test Gap: Useful candidate." in result
    review_files = list((tmp_path / "00_Inbox" / "gap_candidates").glob("local_ai_test_atom_*.md"))
    assert len(review_files) == 1
    review_content = review_files[0].read_text(encoding="utf-8")
    assert "status: PENDING_REVIEW" in review_content
    assert "- [Concept] Test Gap: Useful candidate." in review_content
    assert len(calls) == 1
    prompt, model = calls[0]
    assert model == "gemma3:4b"
    assert "Analyze this Wiki Atom name: test atom" in prompt
    assert "Return ONLY bullet points" in prompt
    assert "If no useful gap exists, return exactly: NONE" in prompt


def test_gap_check_normalizes_unbracketed_type():
    from scripts.mcp_servers.local_ai import _normalize_gap_check_response

    result = _normalize_gap_check_response(
        "- Concept: First-Order Feedback Loop: A reinforcing cycle."
    )

    assert result == "- [Concept] First-Order Feedback Loop: A reinforcing cycle."


def test_parse_gap_line_preserves_hyphenated_name():
    gap_check = load_gap_check_module()

    parsed = gap_check.parse_gap_line("- [Concept] First-Order Feedback Loop: A feedback structure.")

    assert parsed == ("Concept", "First-Order Feedback Loop", "A feedback structure.")


def test_process_and_validate_gaps_preserves_hyphenated_candidate(monkeypatch):
    gap_check = load_gap_check_module()
    monkeypatch.setattr(gap_check, "check_vault_duplicate", lambda canonical_type, name: False)

    result, ignored = gap_check.process_and_validate_gaps(
        "- [Concept] Model-Based Reasoning: A reasoning method.",
        extracted_atoms=[],
    )

    assert result == "- [Concept] Model-Based Reasoning: A reasoning method."
    assert ignored == []


def test_process_and_validate_gaps_filters_illustrative_examples(monkeypatch):
    gap_check = load_gap_check_module()
    monkeypatch.setattr(gap_check, "check_vault_duplicate", lambda canonical_type, name: False)

    result, ignored = gap_check.process_and_validate_gaps(
        "\n".join([
            "- [Entity] Digestive System: An example used to explain systems.",
            "- [Entity] Football Team: An analogy used to explain systems.",
        ]),
        extracted_atoms=[],
    )

    assert result is None
    assert ignored == [
        "Bỏ qua ví dụ minh họa chung chung: [Entity] Digestive System",
        "Bỏ qua ví dụ minh họa chung chung: [Entity] Football Team",
    ]


def test_process_and_validate_gaps_filters_existing_vault_atom(monkeypatch):
    gap_check = load_gap_check_module()
    monkeypatch.setattr(
        gap_check,
        "check_vault_duplicate",
        lambda canonical_type, name: canonical_type == "Concept" and name == "System",
    )

    result, ignored = gap_check.process_and_validate_gaps(
        "- [Concept] System: A set of interconnected elements.",
        extracted_atoms=[],
    )

    assert result is None
    assert ignored == ["Đã tồn tại trong Vault: [Concept] System"]
