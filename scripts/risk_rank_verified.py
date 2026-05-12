import argparse
import json
import os
import sqlite3
from datetime import datetime


def compute_risk(row):
    score = 0
    reasons = []

    confidence = row["confidence"] if row["confidence"] is not None else 0.0
    if confidence < 0.85:
        score += 50
        reasons.append("confidence_violation_low")
    elif confidence < 0.90:
        score += 20
        reasons.append("borderline_confidence")

    if row["learning_source"] == 1:
        score += 20
        reasons.append("learning_source")

    if row["human_review_flag"] == 1:
        score += 15
        reasons.append("already_flagged")

    meta = row["metadata_text"] or ""
    meta_low = meta.lower()
    for token, w in [
        ("conflict", 25),
        ("contradict", 25),
        ("supersede", 15),
        ("ambiguous", 20),
        ("unknown", 15),
    ]:
        if token in meta_low:
            score += w
            reasons.append(f"meta:{token}")

    if not row["file_hash"]:
        score += 10
        reasons.append("missing_file_hash")

    if row["title"] is None or str(row["title"]).strip() == "" or str(row["title"]).strip().lower() == "none":
        score += 10
        reasons.append("missing_or_none_title")

    return score, reasons


def ensure_review_item(conn, item_id, reason):
    c = conn.cursor()
    c.execute("SELECT 1 FROM review_queue WHERE item_id = ? LIMIT 1", (item_id,))
    exists = c.fetchone() is not None
    if not exists:
        c.execute("INSERT INTO review_queue (item_id, reason) VALUES (?, ?)", (item_id, reason))


def main():
    ap = argparse.ArgumentParser(description="Rank VERIFIED atoms by risk and export review list")
    ap.add_argument("--db", required=True, help="Path to wiki_brain.db")
    ap.add_argument("--output", required=True, help="Path to markdown output")
    ap.add_argument("--top-n", type=int, default=20, help="Top N VERIFIED atoms to flag")
    ap.add_argument("--apply-flags", action="store_true", help="Set human_review_flag=1 and enqueue top N")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute(
        """
        SELECT file_id, title, status, confidence, learning_source, human_review_flag, metadata, file_hash
        FROM atoms
        WHERE status = 'VERIFIED'
        """
    )
    rows = c.fetchall()

    ranked = []
    for r in rows:
        d = {
            "file_id": r["file_id"],
            "title": r["title"],
            "status": r["status"],
            "confidence": r["confidence"],
            "learning_source": r["learning_source"],
            "human_review_flag": r["human_review_flag"],
            "metadata_text": json.dumps(r["metadata"], ensure_ascii=False) if r["metadata"] is not None else "",
            "file_hash": r["file_hash"],
        }
        risk, reasons = compute_risk(d)
        d["risk_score"] = risk
        d["risk_reasons"] = reasons
        ranked.append(d)

    ranked.sort(key=lambda x: (x["risk_score"], 1.0 - (x["confidence"] or 0.0)), reverse=True)
    top = ranked[: max(args.top_n, 0)]

    if args.apply_flags and top:
        for item in top:
            c.execute(
                "UPDATE atoms SET human_review_flag = 1 WHERE file_id = ?",
                (item["file_id"],),
            )
            reason = (
                f"Priority review (risk_score={item['risk_score']}): "
                + ", ".join(item["risk_reasons"][:5])
            )
            ensure_review_item(conn, item["file_id"], reason)
        conn.commit()

    c.execute(
        """
        SELECT rq.item_id, rq.reason, rq.added_at, a.status, a.confidence, a.human_review_flag
        FROM review_queue rq
        LEFT JOIN atoms a ON a.file_id = rq.item_id
        ORDER BY rq.added_at DESC
        """
    )
    queue_rows = c.fetchall()
    conn.close()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = []
    lines.append(f"# Priority Review Queue ({now})")
    lines.append("")
    lines.append(f"- VERIFIED scanned: {len(ranked)}")
    lines.append(f"- Top-N selected: {len(top)}")
    lines.append(f"- apply_flags: {'YES' if args.apply_flags else 'NO'}")
    lines.append(f"- Review queue total: {len(queue_rows)}")
    lines.append("")
    lines.append("## Top Risk VERIFIED")
    lines.append("")
    lines.append("| # | Risk | Confidence | File ID | Title | Reasons |")
    lines.append("|---|---:|---:|---|---|---|")
    for i, item in enumerate(top, start=1):
        lines.append(
            f"| {i} | {item['risk_score']} | {item['confidence'] or 0:.4f} | "
            f"{item['file_id']} | {str(item['title'] or '').replace('|', '/')} | "
            f"{', '.join(item['risk_reasons'][:6])} |"
        )

    lines.append("")
    lines.append("## Current Review Queue (DB)")
    lines.append("")
    lines.append("| # | Item ID | Status | Confidence | Human Flag | Added At | Reason |")
    lines.append("|---|---|---|---:|---:|---|---|")
    for i, r in enumerate(queue_rows, start=1):
        lines.append(
            f"| {i} | {r['item_id']} | {r['status'] or ''} | "
            f"{(r['confidence'] if r['confidence'] is not None else 0):.4f} | "
            f"{r['human_review_flag'] if r['human_review_flag'] is not None else 0} | "
            f"{r['added_at'] or ''} | {str(r['reason'] or '').replace('|', '/')} |"
        )

    with open(args.output, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")

    print(f"wrote: {args.output}")
    print(f"verified_scanned={len(ranked)} top_n={len(top)} queue_total={len(queue_rows)}")


if __name__ == "__main__":
    main()

