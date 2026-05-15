from __future__ import annotations

import argparse
import pathlib
import re
import sys


def _read_text(path: pathlib.Path | None) -> str:
    if not path or not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _extract_value(text: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*\"?([^\n\"]+)\"?", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def _report_state(path: pathlib.Path | None, required_key: str, required_value: str | None = None) -> tuple[bool, str]:
    if not path or not path.exists():
        return False, "MISSING"

    text = _read_text(path)
    value = _extract_value(text, required_key)
    if value is None:
        return False, f"MALFORMED:{required_key}"

    if required_value is not None and value != required_value:
        return False, value

    return True, value


def _resolve(args) -> tuple[dict[str, str], dict[str, str], int]:
    prep_ok, prep_state = _report_state(args.source_prep, "staging_status", "READY")
    audit_ok, audit_state = _report_state(args.source_audit, "audit_status", "PASSED")
    audit_lock_ok, audit_lock_state = _report_state(args.source_audit, "ready_for_input_lock", "YES")
    lock_ok, lock_state = _report_state(args.input_lock, "status", "READY")
    orch_ok, orch_state = _report_state(args.orchestration, "status", "READY_FOR_GENERATE")
    gen_ok, gen_state = _report_state(args.generate, "status", "DONE")
    close_ok, close_state = _report_state(args.closeout, "status", "DONE")

    precheck = {
        "source_prep_report": "YES" if args.source_prep and pathlib.Path(args.source_prep).exists() else "NO",
        "source_audit_report": "YES" if args.source_audit and pathlib.Path(args.source_audit).exists() else "NO",
        "ingest_input_lock": "YES" if args.input_lock and pathlib.Path(args.input_lock).exists() else "NO",
        "ingest_orchestration_report": "YES" if args.orchestration and pathlib.Path(args.orchestration).exists() else "NO",
        "ingest_generate_report": "YES" if args.generate and pathlib.Path(args.generate).exists() else "NO",
        "ingest_closeout_report": "YES" if args.closeout and pathlib.Path(args.closeout).exists() else "NO",
    }

    # Invalid or failed artifacts block immediately at their own stage.
    if args.source_prep and not prep_ok:
        report = {
            "current_stage": "prepare-source",
            "next_stage": "prepare-source",
            "lifecycle_status": "BLOCKED",
            "fail_reason": f"SOURCE PREP REPORT not READY ({prep_state})",
        }
        return precheck, report, 1

    if args.source_audit and (not audit_ok or not audit_lock_ok):
        detail = audit_state if not audit_ok else audit_lock_state
        report = {
            "current_stage": "audit-promote-source",
            "next_stage": "audit-promote-source",
            "lifecycle_status": "BLOCKED",
            "fail_reason": f"SOURCE AUDIT REPORT not ready for input lock ({detail})",
        }
        return precheck, report, 1

    if args.input_lock and not lock_ok:
        report = {
            "current_stage": "lock-ingest-input",
            "next_stage": "lock-ingest-input",
            "lifecycle_status": "BLOCKED",
            "fail_reason": f"INGEST INPUT LOCK not READY ({lock_state})",
        }
        return precheck, report, 1

    if args.orchestration and not orch_ok:
        report = {
            "current_stage": "ingest",
            "next_stage": "ingest",
            "lifecycle_status": "BLOCKED",
            "fail_reason": f"INGEST ORCHESTRATION REPORT not READY_FOR_GENERATE ({orch_state})",
        }
        return precheck, report, 1

    if args.generate and not gen_ok:
        report = {
            "current_stage": "ingest-generate",
            "next_stage": "ingest-generate",
            "lifecycle_status": "BLOCKED",
            "fail_reason": f"INGEST GENERATE REPORT not DONE ({gen_state})",
        }
        return precheck, report, 1

    if args.closeout and not close_ok:
        report = {
            "current_stage": "ingest-index-log",
            "next_stage": "ingest-index-log",
            "lifecycle_status": "BLOCKED",
            "fail_reason": f"INGEST CLOSEOUT REPORT not DONE ({close_state})",
        }
        return precheck, report, 1

    # Fresh or resumed path resolution by artifact presence.
    if not args.source_prep:
        report = {
            "current_stage": "NONE",
            "next_stage": "prepare-source",
            "lifecycle_status": "IN_PROGRESS",
            "fail_reason": "NONE",
        }
        return precheck, report, 0

    if not args.source_audit:
        report = {
            "current_stage": "prepare-source",
            "next_stage": "audit-promote-source",
            "lifecycle_status": "IN_PROGRESS",
            "fail_reason": "NONE",
        }
        return precheck, report, 0

    if not args.input_lock:
        report = {
            "current_stage": "audit-promote-source",
            "next_stage": "lock-ingest-input",
            "lifecycle_status": "IN_PROGRESS",
            "fail_reason": "NONE",
        }
        return precheck, report, 0

    if not args.orchestration:
        report = {
            "current_stage": "lock-ingest-input",
            "next_stage": "ingest",
            "lifecycle_status": "IN_PROGRESS",
            "fail_reason": "NONE",
        }
        return precheck, report, 0

    if not args.generate:
        report = {
            "current_stage": "ingest",
            "next_stage": "ingest-generate",
            "lifecycle_status": "IN_PROGRESS",
            "fail_reason": "NONE",
        }
        return precheck, report, 0

    if not args.closeout:
        report = {
            "current_stage": "ingest-generate",
            "next_stage": "ingest-index-log",
            "lifecycle_status": "IN_PROGRESS",
            "fail_reason": "NONE",
        }
        return precheck, report, 0

    report = {
        "current_stage": "ingest-index-log",
        "next_stage": "DONE",
        "lifecycle_status": "DONE",
        "fail_reason": "NONE",
    }
    return precheck, report, 0


def _print_report(precheck: dict[str, str], report: dict[str, str], mode: str) -> None:
    print("LIFECYCLE PRECHECK:")
    for key, value in precheck.items():
        print(f"  {key}: \"{value}\"")
    print(f"  next_stage: \"{report['next_stage']}\"")
    print(f"  status: \"{'BLOCKED' if report['lifecycle_status'] == 'BLOCKED' else 'READY'}\"")
    print("")
    print("INGEST LIFECYCLE REPORT:")
    print('  source_id: "UNKNOWN"')
    print(f'  current_stage: "{report["current_stage"]}"')
    print(f'  next_stage: "{report["next_stage"]}"')
    print(f'  mode: "{mode}"')
    print(f'  lifecycle_status: "{report["lifecycle_status"]}"')
    print('  final_artifact: "NONE"')
    print(f'  fail_reason: "{report["fail_reason"]}"')


def main() -> None:
    parser = argparse.ArgumentParser(description="Check ingest lifecycle artifact gates and resolve next stage.")
    parser.add_argument("--mode", default="guided", choices=["guided", "fast-path"])
    parser.add_argument("--source-prep")
    parser.add_argument("--source-audit")
    parser.add_argument("--input-lock")
    parser.add_argument("--orchestration")
    parser.add_argument("--generate")
    parser.add_argument("--closeout")
    args = parser.parse_args()

    # Normalize path strings to Path or None.
    for field in ["source_prep", "source_audit", "input_lock", "orchestration", "generate", "closeout"]:
        value = getattr(args, field)
        setattr(args, field, pathlib.Path(value) if value else None)

    precheck, report, exit_code = _resolve(args)
    _print_report(precheck, report, args.mode)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
