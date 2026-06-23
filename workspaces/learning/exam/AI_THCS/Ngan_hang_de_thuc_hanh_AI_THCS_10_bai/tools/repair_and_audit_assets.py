from __future__ import annotations

import json
import os
import shutil
import tempfile
import uuid
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

PACKAGE_DIR = Path(__file__).resolve().parents[1]
MEDIA_DIR = PACKAGE_DIR / "Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media"
XHTML_NS = "http://www.w3.org/1999/xhtml"
ET.register_namespace("", XHTML_NS)


def write_blockly_xml(tree: ET.ElementTree, xml_path: Path) -> None:
    text = ET.tostring(tree.getroot(), encoding="unicode")
    text = text.replace(' xmlns:html="http://www.w3.org/1999/xhtml"', "")
    text = text.replace("<html:", "<").replace("</html:", "</")
    if text.startswith("<xml ") and "xmlns=" not in text.split(">", 1)[0]:
        text = text.replace("<xml ", f'<xml xmlns="{XHTML_NS}" ', 1)
    elif text.startswith("<xml>"):
        text = text.replace("<xml>", f'<xml xmlns="{XHTML_NS}">', 1)
    xml_path.write_text(text, encoding="utf-8")


def read_project(sb3_path: Path) -> tuple[dict, dict[str, bytes]]:
    extras: dict[str, bytes] = {}
    with zipfile.ZipFile(sb3_path, "r") as archive:
        project = json.loads(archive.read("project.json").decode("utf-8"))
        for name in archive.namelist():
            if name != "project.json":
                extras[name] = archive.read(name)
    return project, extras


def write_project(sb3_path: Path, project: dict, extras: dict[str, bytes]) -> None:
    fd, tmp_name = tempfile.mkstemp(suffix=".sb3")
    os.close(fd)
    tmp = Path(tmp_name)
    try:
        with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("project.json", json.dumps(project, ensure_ascii=False, separators=(",", ":")))
            for name, data in extras.items():
                archive.writestr(name, data)
        shutil.move(str(tmp), sb3_path)
    finally:
        if tmp.exists():
            tmp.unlink()


def stage(project: dict) -> dict:
    return next(target for target in project["targets"] if target.get("isStage"))


def sprites(project: dict) -> list[dict]:
    return [target for target in project["targets"] if not target.get("isStage")]


def clone_costume(costume: dict, name: str) -> dict:
    cloned = dict(costume)
    cloned["name"] = name
    return cloned


def ensure_costumes(target: dict, names: list[str]) -> None:
    costumes = target.get("costumes", [])
    if not costumes:
        return
    base = costumes[0]
    while len(costumes) < len(names):
        costumes.append(clone_costume(base, names[len(costumes)]))
    for costume, name in zip(costumes, names):
        costume["name"] = name


def ensure_backdrops(stage_target: dict, names: list[str]) -> None:
    costumes = stage_target.get("costumes", [])
    if not costumes:
        return
    base = costumes[0]
    while len(costumes) < len(names):
        costumes.append(clone_costume(base, names[len(costumes)]))
    for costume, name in zip(costumes, names):
        costume["name"] = name


def rename_costume_fields(project: dict, mapping: dict[str, str]) -> None:
    for target in project["targets"]:
        for block in target.get("blocks", {}).values():
            if not isinstance(block, dict):
                continue
            fields = block.get("fields", {})
            value = fields.get("COSTUME")
            if value and value[0] in mapping:
                value[0] = mapping[value[0]]


def new_shadow_block(parent_id: str, opcode: str, field_name: str, field_value: str) -> tuple[str, dict]:
    block_id = f"shadow_{uuid.uuid4().hex[:20]}"
    return block_id, {
        "opcode": opcode,
        "next": None,
        "parent": parent_id,
        "inputs": {},
        "fields": {field_name: [field_value, None]},
        "shadow": True,
        "topLevel": False,
    }


def ensure_backdrop_input(target: dict, block_id: str, backdrop: str) -> None:
    block = target.get("blocks", {}).get(block_id)
    if not isinstance(block, dict):
        return
    shadow_id, shadow = new_shadow_block(block_id, "looks_backdrop", "BACKDROP", backdrop)
    target["blocks"][shadow_id] = shadow
    block.setdefault("inputs", {})["BACKDROP"] = [1, shadow_id]


def rename_xml_fields(xml_path: Path, costume_mapping: dict[str, str]) -> None:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for elem in root.iter():
        if elem.tag.split("}")[-1] == "field" and elem.attrib.get("name") == "COSTUME":
            if elem.text in costume_mapping:
                elem.text = costume_mapping[elem.text]
    write_blockly_xml(tree, xml_path)


def ensure_xml_backdrop_inputs(xml_path: Path, mapping: dict[str, str]) -> None:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    ns_uri = root.tag.split("}")[0].strip("{") if root.tag.startswith("{") else ""
    tag = (lambda name: f"{{{ns_uri}}}{name}") if ns_uri else (lambda name: name)
    for block in root.iter():
        if block.tag.split("}")[-1] != "block":
            continue
        block_id = block.attrib.get("id")
        if block.attrib.get("type") != "looks_switchbackdropto" or block_id not in mapping:
            continue
        existing = [
            child for child in list(block)
            if child.tag.split("}")[-1] == "value" and child.attrib.get("name") == "BACKDROP"
        ]
        for child in existing:
            block.remove(child)
        value = ET.Element(tag("value"), {"name": "BACKDROP"})
        shadow = ET.SubElement(value, tag("shadow"), {"type": "looks_backdrop"})
        field = ET.SubElement(shadow, tag("field"), {"name": "BACKDROP"})
        field.text = mapping[block_id]
        block.insert(0, value)
    write_blockly_xml(tree, xml_path)


def collect_blocks(blocks: dict, root_id: str, out: set[str]) -> None:
    if root_id in out or root_id not in blocks or not isinstance(blocks[root_id], dict):
        return
    out.add(root_id)
    block = blocks[root_id]
    for key in ("next", "parent"):
        value = block.get(key)
        if key == "next" and isinstance(value, str):
            collect_blocks(blocks, value, out)
    for input_value in block.get("inputs", {}).values():
        if isinstance(input_value, list):
            for item in input_value[1:]:
                if isinstance(item, str):
                    collect_blocks(blocks, item, out)
    for mutation_value in block.get("mutation", {}).values():
        if isinstance(mutation_value, str) and mutation_value in blocks:
            collect_blocks(blocks, mutation_value, out)


def split_sprite_by_roots(project: dict, groups: list[tuple[str, list[str]]], costume_names: list[str]) -> None:
    source = sprites(project)[0]
    source_blocks = source.get("blocks", {})
    new_targets = [stage(project)]
    for name, root_ids in groups:
        target = dict(source)
        target["name"] = name
        target["blocks"] = {}
        target["comments"] = {}
        target["currentCostume"] = 0
        target["layerOrder"] = len(new_targets)
        target["costumes"] = [dict(costume) for costume in source.get("costumes", [])]
        ensure_costumes(target, costume_names)
        keep: set[str] = set()
        for root_id in root_ids:
            collect_blocks(source_blocks, root_id, keep)
        target["blocks"] = {block_id: source_blocks[block_id] for block_id in keep if block_id in source_blocks}
        for block in target["blocks"].values():
            if isinstance(block, dict) and block.get("parent") not in target["blocks"]:
                block["parent"] = None
        new_targets.append(target)
    project["targets"] = new_targets


def repair_project(item: int) -> None:
    sb3_path = MEDIA_DIR / f"bt{item}_code.sb3"
    xml_path = MEDIA_DIR / f"bt{item}_code.xml"
    project, extras = read_project(sb3_path)
    stg = stage(project)
    sprs = sprites(project)
    if not sprs:
        return

    if item == 1:
        ensure_costumes(sprs[0], ["waiting", "dung", "sai", "extra"])
        mapping = {"cho": "waiting"}
        rename_costume_fields(project, mapping)
        rename_xml_fields(xml_path, mapping)

    if item == 2:
        mapping = {
            "bt2_backdrop1": "Forest",
            "bt2_backdrop2": "Woods",
            "bt2_backdrop3": "Blue Sky",
            "bt2_backdrop4": "Farm",
        }
        ensure_backdrops(stg, ["backdrop1", "Forest", "Woods", "Blue Sky", "Farm"])
        for target in sprs:
            for block_id, backdrop in mapping.items():
                ensure_backdrop_input(target, block_id, backdrop)
        ensure_xml_backdrop_inputs(xml_path, mapping)

    if item == 5:
        ensure_costumes(sprs[0], ["waiting", "smile", "sad", "surprise"])
        ensure_backdrops(stg, ["neutral", "smile", "sad", "surprise"])
        mapping = {"cho": "waiting", "vui": "smile", "buon": "sad", "ngac nhien": "surprise"}
        rename_costume_fields(project, mapping)
        rename_xml_fields(xml_path, mapping)
        backdrop_map = {
            "bt5_backdrop_wait": "neutral",
            "bt5_backdrop_vui": "smile",
            "bt5_backdrop_sad": "sad",
            "bt5_backdrop_surprise": "surprise",
        }
        for block_id, backdrop in backdrop_map.items():
            ensure_backdrop_input(sprs[0], block_id, backdrop)
        ensure_xml_backdrop_inputs(xml_path, backdrop_map)

    if item == 6:
        ensure_costumes(sprs[0], ["exercise", "completed", "extra1", "extra2"])
        mapping = {"dang tap": "exercise", "chuc mung": "completed"}
        rename_costume_fields(project, mapping)
        rename_xml_fields(xml_path, mapping)

    if item == 7:
        ensure_backdrops(stg, ["AI", "Translate", "TeachableMachine", "KetThuc"])
        backdrop_map = {
            "bt7_bg1": "AI",
            "bt7_bg2": "Translate",
            "bt7_bg3": "TeachableMachine",
            "bt7_bg_end": "KetThuc",
        }
        for block_id, backdrop in backdrop_map.items():
            ensure_backdrop_input(sprs[0], block_id, backdrop)
        ensure_xml_backdrop_inputs(xml_path, backdrop_map)

    if item == 8 and len(sprs) == 1:
        split_sprite_by_roots(project, [
            ("Ro", ["bt8_basket_ctrl"]),
            ("Bong", ["bt8_ball_start"]),
            ("DongHo", ["bt8_timer_start"]),
            ("TongKet", ["bt8_on_gameover"]),
        ], ["normal", "highlight", "done", "alert"])

    if item == 9 and len(sprs) == 1:
        split_sprite_by_roots(project, [
            ("Mu", ["bt9_hat_start", "bt9_hat_change"]),
            ("BongTaiTrai", ["bt9_left_ear_start", "bt9_left_ear_change"]),
            ("BongTaiPhai", ["bt9_right_ear_start", "bt9_right_ear_change"]),
            ("Kinh", ["bt9_glasses_start", "bt9_glasses_change"]),
            ("NguoiDan", ["bt9_space"]),
        ], ["style1", "style2", "style3", "style4"])

    write_project(sb3_path, project, extras)


EXPECTED = {
    1: {"ext": {"translate", "text2speech"}, "sprites_min": 1, "costumes": {"waiting", "dung", "sai"}},
    2: {"ext": {"translate", "text2speech"}, "sprites_min": 2, "backdrops_min": 4},
    3: {"ext": {"text2speech"}, "sprites_min": 1},
    4: {"ext": {"translate", "text2speech"}, "lists": {"questions", "answers"}},
    5: {"ext": {"poseFace", "translate", "text2speech"}, "backdrops_min": 3, "costumes": {"waiting", "smile", "sad", "surprise"}},
    6: {"ext": {"poseBody", "text2speech"}, "costumes": {"exercise", "completed"}},
    7: {"ext": {"poseFace", "translate", "text2speech"}, "backdrops_min": 3},
    8: {"ext": {"poseFace", "text2speech"}, "sprites_min": 3, "opcodes": {"poseFace_affdexGoToPart", "event_broadcast"}},
    9: {"ext": {"poseBody", "translate", "text2speech"}, "sprites_min": 5, "opcodes": {"poseBody_goToPart", "event_whenkeypressed"}},
    10: {"ext": {"teachableMachine", "translate", "text2speech"}, "lists": {"presentList"}},
}


def audit_project(item: int) -> list[str]:
    failures: list[str] = []
    sb3_path = MEDIA_DIR / f"bt{item}_code.sb3"
    xml_path = MEDIA_DIR / f"bt{item}_code.xml"
    if not sb3_path.exists() or not xml_path.exists():
        return [f"BT{item}: missing sb3/xml"]
    project, _ = read_project(sb3_path)
    stg = stage(project)
    sprs = sprites(project)
    expected = EXPECTED[item]
    extensions = set(project.get("extensions", []))
    if not expected.get("ext", set()).issubset(extensions):
        failures.append(f"BT{item}: extensions {sorted(extensions)} do not cover {sorted(expected['ext'])}")
    if len(sprs) < expected.get("sprites_min", 0):
        failures.append(f"BT{item}: only {len(sprs)} sprites")
    if len(stg.get("costumes", [])) < expected.get("backdrops_min", 0):
        failures.append(f"BT{item}: only {len(stg.get('costumes', []))} backdrops")
    lists = {value[0] for target in project["targets"] for value in target.get("lists", {}).values()}
    if not expected.get("lists", set()).issubset(lists):
        failures.append(f"BT{item}: lists {sorted(lists)} do not cover {sorted(expected['lists'])}")
    costume_names = {costume["name"] for target in sprs for costume in target.get("costumes", [])}
    if not expected.get("costumes", set()).issubset(costume_names):
        failures.append(f"BT{item}: costumes {sorted(costume_names)} do not cover {sorted(expected['costumes'])}")
    opcodes = {
        block.get("opcode")
        for target in project["targets"]
        for block in target.get("blocks", {}).values()
        if isinstance(block, dict)
    }
    if not expected.get("opcodes", set()).issubset(opcodes):
        failures.append(f"BT{item}: opcodes missing {sorted(expected['opcodes'] - opcodes)}")
    for target in project["targets"]:
        for block_id, block in target.get("blocks", {}).items():
            if isinstance(block, dict) and block.get("opcode") == "looks_switchbackdropto":
                if "BACKDROP" not in block.get("inputs", {}):
                    failures.append(f"BT{item}: {target['name']}:{block_id} missing BACKDROP input")
    return failures


def main() -> int:
    for item in range(1, 11):
        repair_project(item)
    failures: list[str] = []
    for item in range(1, 11):
        failures.extend(audit_project(item))
    if failures:
        print("AUDIT FAIL")
        for failure in failures:
            print(failure)
        return 1
    print("AUDIT PASS: BT1-BT10 static asset checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
