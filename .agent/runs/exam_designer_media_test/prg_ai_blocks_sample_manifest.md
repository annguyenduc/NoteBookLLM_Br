---
asset_id: "MEDIA_PRG_AI_BLOCKS_Q01_001"
file_name: "prg_ai_blocks_sample.png"
type: "image"
source_tool: "PRG AI Blocks"
source_url: "https://playground.raise.mit.edu/create/"
generation_method: "tool_api_generated"
source_file: "prg_ai_blocks_sample.xml"
reproduction_guide: "README_REPRODUCE_PRG_AI_BLOCKS_MEDIA.md"
used_in: "Sample question: observe block code and predict behavior"
purpose: "Preview generated code-sample media for @exam-designer rule validation"
answer_leak_check: "NEEDS_REVIEW"
review_status: "PREVIEW_ONLY"
canonical_status: "NON_CANONICAL"
---

# PRG AI Blocks Sample Manifest

Generated in the real PRG AI Blocks page via Playwright + Blockly workspace XML.

## Reproduction Steps
See also: `README_REPRODUCE_PRG_AI_BLOCKS_MEDIA.md`.

1. Open `https://playground.raise.mit.edu/create/`.
2. Load Blockly XML from `prg_ai_blocks_sample.xml` into the main workspace.
3. Capture workspace screenshot as `prg_ai_blocks_sample.png`.

## Code Behavior
When the green flag is clicked:
1. The sprite asks: "Công nghệ nào giúp máy tính nhận biết mẫu từ dữ liệu?"
2. If `answer = AI`, the sprite says: "Đúng! AI có thể học mẫu từ dữ liệu." for 2 seconds.

## Review Notes
- This is a preview asset, not a canonical assessment asset.
- Human should confirm wording, answer-leak status, and visual clarity before using in a real test.
