# CONTINUITY.md

current_state: "Đã bổ sung E9 GENERATED TOOL MEDIA RULES cho @exam-designer và tạo thử media preview từ PRG AI Blocks. Đã thêm hướng dẫn tái lập đầy đủ tại .agent/runs/exam_designer_media_test/README_REPRODUCE_PRG_AI_BLOCKS_MEDIA.md để agent sau mở PRG AI Blocks, dùng Playwright + Blockly XML, chụp screenshot, lưu XML/source, viết manifest, và cleanup dependency probe mà không phải suy luận lại. Manifest prg_ai_blocks_sample_manifest.md đã trỏ về reproduction guide."
next_step_for_AN: "Review rule E9, ảnh preview PRG AI Blocks, và README tái lập; nếu ổn thì chọn có stage cả .agent/runs/exam_designer_media_test/ làm evidence hay chỉ stage rule/agent files, sau đó commit và merge branch agent/20260610-exam-designer-agent vào main."
blockers: []
verification:
  - "git diff --check: pass"
  - "python tomllib parse .codex/agents/exam-designer.toml: TOML_OK exam-designer"
  - "Select-String confirmed README includes PREVIEW_ONLY/NON_CANONICAL, window.Blockly.getMainWorkspace, npx.cmd, playwright install chromium, tool_api_generated manifest, and Known Failure Modes"
  - "Select-String confirmed manifest has reproduction_guide: README_REPRODUCE_PRG_AI_BLOCKS_MEDIA.md"
  - "git status shows expected branch agent/20260610-exam-designer-agent and expected changed/untracked files"
