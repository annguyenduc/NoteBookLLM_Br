#!/usr/bin/env python3
"""
OhStem App Blockly-style SVG renderer.

Màu và hình dạng block dựa trên:
- Ảnh giao diện thật OhStem App (app.ohstem.vn)
- Source code AITT-VN GitHub (definition.js các extension repos)

Block shapes dùng SVG path chuẩn Blockly:
- Hat block (event): đỉnh tròn, không có notch trên
- Statement block: có notch trên và tab dưới
- C-block (loop): có khoang bên trong
"""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = (
    "asset_id", "title", "source_tool", "source_url",
    "used_in", "purpose", "answer_leak_check", "review_status",
    "program", "question",
)

CATEGORY_COLORS: dict[str, tuple[str, str]] = {
    # AITT-VN/yolouno_extension_robotics definition.js and toolbox.xml.
    "root":     ("#717171", "#4f4f4f"),
    "robot":    ("#ff4ccd", "#b83291"),
    "drivebase":("#ff4ccd", "#b83291"),
    "motor":    ("#0090f5", "#0067b3"),
    "servo":    ("#0090f5", "#0067b3"),
    "sensor":   ("#9b6af6", "#6d46ba"),
    "line":     ("#34ccf1", "#1f8faa"),
    "line_sensor":("#34ccf1", "#1f8faa"),
    "follow_line":("#34ccf1", "#1f8faa"),

    # General OhStem/Scratch-like fallback categories.
    "basic":    ("#4C97FF", "#3373CC"),  # CƠ BẢN — xanh dương (Scratch blue)
    "event":    ("#4C97FF", "#3373CC"),  # bắt đầu thuộc CƠ BẢN
    "input":    ("#FF6680", "#CC2244"),  # NGÕ VÀO — hồng neon
    "music":    ("#CF63CF", "#9A2F9A"),  # ÂM NHẠC — tím hồng
    "led":      ("#9966FF", "#6633CC"),  # LED — tím
    "bluetooth":("#FF69B4", "#CC2277"),  # BLUETOOTH — hồng
    "loop":     ("#59C059", "#389438"),  # VÒNG LẶP — xanh lá
    "logic":    ("#5B67A5", "#3A4578"),  # LÔGIC — xanh thép
    "variable": ("#FFAB19", "#CC7A00"),  # BIẾN — vàng cam
    "math":     ("#59C0A0", "#3A9078"),  # TÍNH TOÁN — xanh ngọc
    "text":     ("#59C0A0", "#3A9078"),  # CHỮ VIẾT — xanh ngọc
    "control":  ("#59C059", "#389438"),  # alias loop
    "action":   ("#4C97FF", "#3373CC"),  # hành động chung — xanh dương
    "rover":    ("#cb2026", "#8B0000"),  # rover ColorBlock
    "xbot_move":("#cb2026", "#8B0000"),  # xBot/Car-style movement preview
}

# ── Blockly SVG geometry constants ──────────────────────────────────────────
BLOCK_W    = 300   # width of a normal statement block
BLOCK_H    = 46    # height of each block row
NOTCH_W    = 30    # width of puzzle notch
NOTCH_H    = 10    # height of puzzle notch
NOTCH_X    = 20    # x position of notch from left
CORNER_R   = 4     # corner radius
SHADOW_H   = 5     # shadow stripe height at bottom of block
HAT_H      = 16    # extra height for hat (event) block top
C_INNER_H  = 30    # height of C-block inner slot
FONT       = "Arial, sans-serif"
FIELD_H    = 34
SEGMENT_GAP = 10


class PackageResult:
    def __init__(self, files: list[Path]) -> None:
        self.files = files


def load_spec(path: Path | str) -> dict[str, Any]:
    spec_path = Path(path)
    data = json.loads(spec_path.read_text(encoding="utf-8"))
    missing = [f for f in REQUIRED_FIELDS if f not in data]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    blocks = data.get("program", {}).get("blocks", [])
    if not blocks:
        raise ValueError("program.blocks must contain at least one block")
    data["_spec_path"] = str(spec_path)
    return data


def asset_basename(spec: dict[str, Any]) -> str:
    raw = str(spec["asset_id"]).strip().lower()
    safe = re.sub(r"[^a-z0-9]+", "_", raw).strip("_")
    if not safe:
        raise ValueError("asset_id cannot be empty")
    return safe


def _hex_darken(hex_color: str, factor: float = 0.7) -> str:
    """Darken a hex color by factor (0-1)."""
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    r, g, b = int(r * factor), int(g * factor), int(b * factor)
    return f"#{r:02x}{g:02x}{b:02x}"


def _get_colors(kind: str) -> tuple[str, str]:
    k = str(kind).lower()
    return CATEGORY_COLORS.get(k, CATEGORY_COLORS["basic"])


def _estimate_text_width(text: str, size: int = 13) -> int:
    return max(12, int(len(text) * size * 0.62))


def _get_block_palette(block: dict[str, Any]) -> tuple[str, str, str]:
    if block.get("fill") and block.get("shadow"):
        fill = str(block["fill"])
        shadow = str(block["shadow"])
    else:
        fill, shadow = _get_colors(str(block.get("kind", "basic")))
    return fill, shadow, _hex_darken(fill, 0.72)


def _get_block_shape(block: dict[str, Any], index: int) -> str:
    shape = str(block.get("shape", "")).lower()
    if shape in {"hat", "statement"}:
        return shape
    return "hat" if index == 0 else "statement"


def _reporter_path(x: float, y: float, w: float, h: float) -> str:
    rx = 4
    tail = 12
    mid = y + h / 2
    return (
        f"M {x + tail} {y} "
        f"H {x + w - rx} Q {x + w} {y} {x + w} {y + rx} "
        f"V {y + h - rx} Q {x + w} {y + h} {x + w - rx} {y + h} "
        f"H {x + tail} "
        f"L {x + tail - 6} {mid + 6} "
        f"L {x} {mid} "
        f"L {x + tail - 6} {mid - 6} "
        f"L {x + tail} {y} Z"
    )


def _slot_field_path(x: float, y: float, w: float, h: float) -> str:
    rx = 4
    nub = 10
    mid = y + h / 2
    return (
        f"M {x + nub} {y} "
        f"H {x + w - nub - rx} Q {x + w - nub} {y} {x + w - nub} {y + rx} "
        f"V {y + h - rx} Q {x + w - nub} {y + h} {x + w - nub - rx} {y + h} "
        f"H {x + nub} "
        f"L {x + nub - 6} {mid + 6} L {x} {mid} L {x + nub - 6} {mid - 6} Z "
        f"M {x + w - nub} {y} "
        f"L {x + w - nub + 6} {mid - 6} L {x + w} {mid} L {x + w - nub + 6} {mid + 6} Z"
    )


def _render_icon_svg(name: str, x: float, y: float, size: int = 28) -> str:
    name = name.lower()
    if name == "pause":
        return f"""
    <g>
      <circle cx="{x + size/2}" cy="{y + size/2}" r="{size/2}" fill="#111111"/>
      <rect x="{x + 8}" y="{y + 7}" width="5" height="14" rx="1" fill="#7dff63"/>
      <rect x="{x + 16}" y="{y + 7}" width="5" height="14" rx="1" fill="#7dff63"/>
    </g>"""
    if name == "stop_hand":
        return f"""
    <g>
      <polygon points="{x+14},{y} {x+24},{y+4} {x+28},{y+14} {x+24},{y+24} {x+14},{y+28} {x+4},{y+24} {x},{y+14} {x+4},{y+4}" fill="#ffb08f" stroke="#111111" stroke-width="1.4"/>
      <text x="{x + 14}" y="{y + 19}" fill="#111111" text-anchor="middle" font-family="{FONT}" font-size="14">✋</text>
    </g>"""
    if name == "wheel":
        return f"""
    <g>
      <circle cx="{x + size/2}" cy="{y + size/2}" r="{size/2 - 1}" fill="#111111"/>
      <circle cx="{x + size/2}" cy="{y + size/2}" r="{size/2 - 6}" fill="none" stroke="#3de3dd" stroke-width="2"/>
      <circle cx="{x + size/2}" cy="{y + size/2}" r="2.4" fill="#3de3dd"/>
      <path d="M {x+14} {y+6} V {y+22} M {x+6} {y+14} H {x+22}" stroke="#3de3dd" stroke-width="1.6" stroke-linecap="round"/>
    </g>"""
    if name == "led_off":
        return f"""
    <g>
      <circle cx="{x + 11}" cy="{y + 14}" r="8" fill="#5b4a83"/>
      <circle cx="{x + 11}" cy="{y + 14}" r="5.5" fill="#7f6dad"/>
      <path d="M {x+23} {y+6} L {x+26} {y+3} M {x+24} {y+12} H {x+29} M {x+23} {y+20} L {x+27} {y+23}" stroke="#ffd34d" stroke-width="2" stroke-linecap="round"/>
      <path d="M {x+20} {y+9} V {y+19}" stroke="#ffd34d" stroke-width="2" stroke-linecap="round"/>
    </g>"""
    if name == "button":
        return f"""
    <g>
      <rect x="{x + 2}" y="{y + 2}" width="24" height="24" rx="4" fill="#f3f6fb" stroke="#9aa9c9"/>
      <circle cx="{x + 14}" cy="{y + 14}" r="6" fill="#111111"/>
      <circle cx="{x + 5}" cy="{y + 5}" r="1.3" fill="#111111"/>
      <circle cx="{x + 23}" cy="{y + 5}" r="1.3" fill="#111111"/>
      <circle cx="{x + 5}" cy="{y + 23}" r="1.3" fill="#111111"/>
      <circle cx="{x + 23}" cy="{y + 23}" r="1.3" fill="#111111"/>
    </g>"""
    return f'<circle cx="{x + size/2}" cy="{y + size/2}" r="{size/2 - 1}" fill="#111111"/>'


def _measure_segment(seg: dict[str, Any]) -> int:
    seg_type = str(seg.get("type", "label")).lower()
    text = str(seg.get("text", ""))
    if seg_type == "icon":
        return 34
    if seg_type == "label":
        return _estimate_text_width(text) + 4
    if seg_type == "dropdown":
        return max(70, _estimate_text_width(text) + 30)
    if seg_type == "number":
        return max(48, _estimate_text_width(text, 16) + 18)
    if seg_type == "reporter":
        return max(180, _estimate_text_width(text) + 56)
    return _estimate_text_width(text)


def _render_segment_svg(seg: dict[str, Any], x: float, y: float, block_fill: str) -> tuple[str, int]:
    seg_type = str(seg.get("type", "label")).lower()
    text = html.escape(str(seg.get("text", "")))
    width = _measure_segment(seg)
    baseline = y + 22

    if seg_type == "icon":
        return _render_icon_svg(str(seg.get("name", "wheel")), x, y + 1, 28), width

    if seg_type == "label":
        svg = f'<text x="{x}" y="{baseline}" fill="#ffffff" font-family="{FONT}" font-size="14" font-weight="bold">{text}</text>'
        return svg, width

    if seg_type == "dropdown":
        display = {"up": "↑", "left": "←", "right": "→", "down": "↓"}.get(str(seg.get("text", "")).lower(), text)
        svg = f"""
    <g>
      <rect x="{x}" y="{y}" width="{width}" height="{FIELD_H}" rx="7" fill="#9de7df"/>
      <text x="{x + width/2 - 6}" y="{baseline}" fill="#111111" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="bold">{display}</text>
      <text x="{x + width - 14}" y="{baseline}" fill="#24b7b1" font-family="{FONT}" font-size="12">▼</text>
    </g>"""
        return svg, width

    if seg_type == "number":
        path = _slot_field_path(x, y + 1, width, FIELD_H - 2)
        svg = f"""
    <g>
      <path d="{path}" fill="#dedcff" stroke="#b8b5ec" stroke-width="1"/>
      <text x="{x + width/2}" y="{baseline}" fill="#111111" text-anchor="middle" font-family="{FONT}" font-size="18">{text}</text>
    </g>"""
        return svg, width

    if seg_type == "reporter":
        fill = str(seg.get("fill", "#62a3f3"))
        shadow = str(seg.get("shadow", "#4d7fc0"))
        icon_name = str(seg.get("icon", "button"))
        path = _reporter_path(x, y, width, FIELD_H)
        icon_svg = _render_icon_svg(icon_name, x + 8, y + 1, 28)
        svg = f"""
    <g>
      <path d="{path}" fill="{fill}" stroke="{shadow}" stroke-width="1"/>
      {icon_svg}
      <text x="{x + 44}" y="{baseline}" fill="#ffffff" font-family="{FONT}" font-size="14" font-weight="bold">{text}</text>
    </g>"""
        return svg, width

    svg = f'<text x="{x}" y="{baseline}" fill="#ffffff" font-family="{FONT}" font-size="13">{text}</text>'
    return svg, width


# ── SVG path builders ────────────────────────────────────────────────────────

def _notch_path(x: float, y: float) -> str:
    """Puzzle notch indent path segment (for top connector slot)."""
    nx = x + NOTCH_X
    return (
        f"H {nx} "
        f"L {nx + 5} {y + NOTCH_H} "
        f"L {nx + 15} {y + NOTCH_H} "
        f"L {nx + NOTCH_W} {y} "
    )


def _notch_bump(x: float, y: float) -> str:
    """Puzzle notch bump path segment (for bottom tab)."""
    nx = x + NOTCH_X
    return (
        f"H {nx + NOTCH_W} "
        f"L {nx + 15} {y + NOTCH_H} "
        f"L {nx + 5} {y + NOTCH_H} "
        f"L {nx} {y} "
    )


def _hat_block_path(x: float, y: float, w: float, h: float) -> str:
    """Hat block shape (event): rounded dome on top, tab on bottom."""
    rx = CORNER_R
    # Top dome with large radius
    path = (
        f"M {x + 10} {y} "
        f"Q {x} {y} {x} {y + 12} "
        f"V {y + h - NOTCH_H} "
    )
    path += _notch_bump(x, y + h - NOTCH_H)
    path += f"H {x + w - rx} Q {x + w} {y + h - NOTCH_H} {x + w} {y + h - NOTCH_H - rx} "
    path += f"V {y + 12} Q {x + w} {y} {x + w - 10} {y} Z"
    return path


def _statement_block_path(x: float, y: float, w: float, h: float, has_prev: bool = True) -> str:
    """Normal statement block: notch on top (if has_prev), tab on bottom."""
    rx = CORNER_R
    bot = y + h - NOTCH_H

    # Start top-left
    path = f"M {x + rx} {y} "

    # Top edge with optional notch indent
    if has_prev:
        path += _notch_path(x, y)
    path += f"H {x + w - rx} Q {x + w} {y} {x + w} {y + rx} "

    # Right edge
    path += f"V {bot - rx} Q {x + w} {bot} {x + w - rx} {bot} "

    # Bottom edge with tab bump
    path += _notch_bump(x, bot)
    path += f"H {x + rx} Q {x} {bot} {x} {bot - rx} "

    # Left edge back to start
    path += f"V {y + rx} Q {x} {y} {x + rx} {y} Z"
    return path


def _shadow_path(x: float, y: float, w: float, h: float, is_hat: bool = False) -> str:
    """Shadow stripe at bottom of block."""
    sy = y + h - SHADOW_H - NOTCH_H
    ey = y + h - NOTCH_H
    rx = CORNER_R
    return (
        f"M {x + (10 if is_hat else rx)} {sy} "
        f"H {x + w - rx} Q {x + w} {sy} {x + w} {sy + rx} "
        f"V {ey - rx} Q {x + w} {ey} {x + w - rx} {ey} "
        f"H {x + NOTCH_X + NOTCH_W} "
        f"L {x + NOTCH_X + 15} {ey + NOTCH_H} "
        f"L {x + NOTCH_X + 5} {ey + NOTCH_H} "
        f"L {x + NOTCH_X} {ey} "
        f"H {x + rx} Q {x} {ey} {x} {ey - rx} "
        f"V {sy + rx} Q {x} {sy} {x + rx} {sy} Z"
    )


def render_block_svg_group(
    block: dict[str, Any],
    index: int,
    x: float,
    y: float,
    is_first: bool,
) -> tuple[str, float, float]:
    """
    Render một block đơn lẻ thành SVG <g> group.
    Trả về (svg_string, height_used).
    """
    kind = str(block.get("kind", "basic")).lower()
    label = html.escape(str(block.get("label", f"Block {index + 1}")))
    fill, shadow, dark = _get_block_palette(block)
    shape = _get_block_shape(block, index)
    is_hat = shape == "hat"
    h = BLOCK_H + (HAT_H if is_hat else 0)
    segments = block.get("segments", [])
    if segments:
        segment_widths = [_measure_segment(seg) for seg in segments]
        w = max(BLOCK_W, 28 + sum(segment_widths) + SEGMENT_GAP * (len(segment_widths) - 1) + 18)
    else:
        w = max(BLOCK_W, _estimate_text_width(html.unescape(label)) + 34)

    if is_hat:
        main_path = _hat_block_path(x, y, w, h)
    else:
        main_path = _statement_block_path(x, y, w, h, has_prev=True)

    shadow_path = _shadow_path(x, y, w, h, is_hat=is_hat)

    content_y = y + max(4, (h - NOTCH_H - FIELD_H) / 2)
    content_parts: list[str] = []
    if segments:
        cursor = x + 14
        for seg in segments:
            seg_svg, seg_width = _render_segment_svg(seg, cursor, content_y, fill)
            content_parts.append(seg_svg)
            cursor += seg_width + SEGMENT_GAP
    else:
        text_y = y + (h - NOTCH_H) / 2 + 5
        content_parts.append(
            f'<text x="{x + 12}" y="{text_y}" fill="#ffffff" font-family="{FONT}" font-size="14" font-weight="bold">{label}</text>'
        )

    group = f"""  <g role="listitem" aria-label="{label}">
    <path d="{main_path}" fill="{fill}" stroke="{dark}" stroke-width="1"/>
    <path d="{shadow_path}" fill="{dark}" opacity="0.4"/>
{''.join(content_parts)}
  </g>"""

    return group, h, w


def render_svg(spec: dict[str, Any]) -> str:
    canvas   = spec.get("canvas", {})
    width    = int(canvas.get("width", 640))
    height   = int(canvas.get("height", 480))
    title    = html.escape(str(spec["title"]))
    device   = html.escape(str(spec.get("program", {}).get("device", "Yolo:Bit")))
    blocks   = spec["program"]["blocks"]
    prompt   = html.escape(str(spec.get("question", {}).get("prompt", "")))
    alt_text = html.escape(str(spec.get("question", {}).get("alt_text", "")))

    # ── Tính toán layout ────────────────────────────────────────────────────
    start_x = 40
    start_y = 50
    gap     = 0   # Blockly blocks connect directly, no gap

    groups: list[str] = []
    cur_y = start_y
    max_block_w = BLOCK_W
    for i, block in enumerate(blocks):
        g, h, w = render_block_svg_group(block, i, start_x, cur_y, i == 0)
        groups.append(g)
        cur_y += h - NOTCH_H  # blocks overlap at notch
        max_block_w = max(max_block_w, w)

    # Auto-size canvas to fit blocks + margins
    content_h = cur_y - start_y + NOTCH_H + 60
    canvas_h = max(height, content_h)
    canvas_w = max(width, int(max_block_w + start_x + 40))

    # ── Build SVG ───────────────────────────────────────────────────────────
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
     width="{canvas_w}" height="{canvas_h}"
     viewBox="0 0 {canvas_w} {canvas_h}"
     role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">{alt_text}</desc>
  <rect width="{canvas_w}" height="{canvas_h}" fill="#f9f9f9"/>

  <!-- PREVIEW watermark -->
  <text x="{canvas_w - 10}" y="14" fill="#cccccc"
        font-family="{FONT}" font-size="10"
        text-anchor="end">PREVIEW_ONLY / NON_CANONICAL · {device}</text>

  <!-- Blocks -->
  <g role="list">
{''.join(groups)}
  </g>

  <!-- Question prompt box -->
  <rect x="{start_x}" y="{cur_y + 10}" width="{max_block_w}" height="30"
        rx="4" fill="#e8f4fd" stroke="#c0d8f0" stroke-width="1"/>
  <text x="{start_x + 8}" y="{cur_y + 29}" fill="#1a5276"
        font-family="{FONT}" font-size="11">{prompt}</text>
</svg>
'''
    return svg


def render_html_preview(spec: dict[str, Any], svg_file_name: str) -> str:
    title    = html.escape(str(spec["title"]))
    alt_text = html.escape(str(spec.get("question", {}).get("alt_text", "")))
    prompt   = html.escape(str(spec.get("question", {}).get("prompt", "")))
    return f'''<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    body {{ margin: 0; font-family: Arial, sans-serif; background: #f0f0f0; color: #1f2933; }}
    main {{ max-width: 800px; margin: 24px auto; padding: 0 16px; }}
    h1 {{ font-size: 18px; margin-bottom: 8px; }}
    .frame {{ background: #fff; border: 1px solid #ddd; padding: 16px; display: inline-block; }}
    img {{ display: block; max-width: 100%; height: auto; }}
    .meta {{ margin-top: 12px; font-size: 13px; color: #52606d; }}
    .badge {{ display: inline-block; background: #fff3cd; border: 1px solid #ffc107;
              color: #856404; font-size: 11px; padding: 2px 6px; border-radius: 3px; }}
  </style>
</head>
<body>
  <main>
    <h1>{title}</h1>
    <span class="badge">PREVIEW_ONLY / NON_CANONICAL</span>
    <div class="frame" style="margin-top:10px">
      <img src="{html.escape(svg_file_name)}" alt="{alt_text}">
    </div>
    <p class="meta"><strong>Câu hỏi:</strong> {prompt}</p>
    <p class="meta">Human review bắt buộc trước khi đưa vào đề thi chính thức.</p>
  </main>
</body>
</html>
'''


def render_manifest(spec: dict[str, Any], svg_file_name: str) -> str:
    source_file = Path(str(spec.get("_spec_path", "spec.json"))).name
    return f'''---
asset_id: "{spec["asset_id"]}"
file_name: "{svg_file_name}"
html_preview: "{Path(svg_file_name).with_suffix(".html").name}"
type: "image/svg"
source_tool: "{spec["source_tool"]}"
source_url: "{spec["source_url"]}"
generation_method: "local_ohstem_style_renderer_preview"
source_file: "{source_file}"
used_in: "{spec["used_in"]}"
purpose: "{spec["purpose"]}"
answer_leak_check: "{spec["answer_leak_check"]}"
review_status: "{spec["review_status"]}"
canonical_status: "NON_CANONICAL"
human_review_required: "YES"
---

# {spec["asset_id"]} Manifest

This asset is a local OhStem-style renderer preview for assessment drafting.
It is NOT a real OhStem App screenshot and must not be treated as canonical evidence.

## Review Notes

- Confirm visual matches intended OhStem task before learner release.
- Confirm block labels do not reveal the answer accidentally.
- Replace with real tool screenshot when official publication requires source-tool evidence.
'''


def render_quarto_template(spec: dict[str, Any], svg_file_name: str) -> str:
    title    = str(spec["title"])
    prompt   = str(spec.get("question", {}).get("prompt", ""))
    alt_text = str(spec.get("question", {}).get("alt_text", "OhStem preview media."))
    return f'''---
title: "{title}"
lang: vi
format:
  html:
    toc: false
    embed-resources: true
  docx:
    reference-doc: null
---

::: {{.callout-note}}
Status: `PREVIEW_ASSESSMENT`, `PREVIEW_ONLY`, `NON_CANONICAL`.
:::

## Media Prompt

{prompt}

![{alt_text}]({svg_file_name}){{fig-alt="{alt_text}"}}

## Export Commands

```powershell
quarto render exam_export.qmd --to html
quarto render exam_export.qmd --to docx
```
'''


def render_pandoc_template(spec: dict[str, Any], svg_file_name: str) -> str:
    title    = str(spec["title"])
    prompt   = str(spec.get("question", {}).get("prompt", ""))
    alt_text = str(spec.get("question", {}).get("alt_text", "OhStem preview media."))
    return f'''---
title: "{title}"
lang: vi
---

> Status: `PREVIEW_ASSESSMENT`, `PREVIEW_ONLY`, `NON_CANONICAL`.

## Media Prompt

{prompt}

![{alt_text}]({svg_file_name})

## Pandoc Export

```powershell
pandoc exam_export.pandoc.md --resource-path=. --standalone -o exam_export.html
pandoc exam_export.pandoc.md --resource-path=. --standalone -o exam_export.docx
```
'''


def write_package(spec_path: Path | str, output_dir: Path | str) -> PackageResult:
    spec = load_spec(spec_path)
    out  = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    base         = asset_basename(spec)
    svg_name     = f"{base}.svg"
    html_name    = f"{base}.html"
    manifest_name = f"{base}_manifest.md"

    files = [
        out / svg_name,
        out / html_name,
        out / manifest_name,
        out / "exam_export.qmd",
        out / "exam_export.pandoc.md",
    ]

    files[0].write_text(render_svg(spec),                             encoding="utf-8")
    files[1].write_text(render_html_preview(spec, svg_name),          encoding="utf-8")
    files[2].write_text(render_manifest(spec, svg_name),              encoding="utf-8")
    files[3].write_text(render_quarto_template(spec, svg_name),       encoding="utf-8")
    files[4].write_text(render_pandoc_template(spec, svg_name),       encoding="utf-8")
    return PackageResult(files)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render a non-canonical OhStem exam media preview package."
    )
    parser.add_argument("--spec", required=True, help="Path to an OhStem media JSON spec.")
    parser.add_argument("--out",  required=True, help="Output directory for the preview package.")
    return parser.parse_args()


def main() -> int:
    args   = parse_args()
    result = write_package(args.spec, args.out)
    for path in result.files:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
