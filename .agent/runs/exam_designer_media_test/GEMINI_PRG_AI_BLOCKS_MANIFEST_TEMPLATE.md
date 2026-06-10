---
asset_id: "MEDIA_PRG_AI_BLOCKS_QXX_001"
file_name: "cau_xx.raw.png"
annotated_file_name: "cau_xx.annotated.png"
type: "image"
source_tool: "PRG AI Blocks"
source_url: "https://playground.raise.mit.edu/create/"
generation_method: "real_tool_blockly_xml_injection"
source_file: "cau_xx.xml"
reproduction_guide: "README_REPRODUCE_PRG_AI_BLOCKS_MEDIA.md"
sop_file: "GEMINI_PRG_AI_BLOCKS_MEDIA_SOP.md"
used_in: "Cau XX"
purpose: "Real tool screenshot for assessment media"
extension_loading_required: "NO"
extensions_loaded:
  - ""
answer_leak_check: "NEEDS_REVIEW"
review_status: "PREVIEW_ONLY"
canonical_status: "NON_CANONICAL"
human_review_required: "YES"
---

# PRG AI Blocks Manifest Template

## Required Notes

- `file_name` must point to the raw screenshot, not the annotated screenshot.
- Set `extension_loading_required` to `YES` only if direct XML injection failed and UI loading was needed.
- If extensions were loaded, list them under `extensions_loaded`.
- `answer_leak_check` must be reviewed before exam use.
- `review_status` must remain `PREVIEW_ONLY` until a human approves the asset.

## Minimal Reproduction Log

1. Open `https://playground.raise.mit.edu/create/`.
2. Wait for `window.Blockly.getMainWorkspace()`.
3. Clear workspace.
4. Inject XML from `source_file`.
5. If block types are missing, load required extension and retry.
6. Save raw screenshot to `file_name`.
7. Save rendered XML.
8. If needed, create `annotated_file_name` as a second file.

## Review Checklist

- raw screenshot exists
- XML exists
- manifest exists
- screenshot came from real PRG AI Blocks
- block text is readable
- asset does not unintentionally reveal the answer
- human review completed before official use
