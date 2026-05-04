import datetime
import io
import os
import re
import shutil
import subprocess
import sys

# Force UTF-8 stdout/stderr on Windows to avoid mojibake in helper output.
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding != "utf-8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

WIKI_DIR = r"d:\NoteBookLLM_Br\3-resources\wiki"
OVERVIEW_PATH = os.path.join(WIKI_DIR, "overview.md")
INDEX_PATH = os.path.join(WIKI_DIR, "index.md")
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))

CATEGORIES = {
    "THINK": "THINK_",
    "STATS": "STAT_",
    "SQL": "SQL_",
    "PYTHON": "PY_",
    "VISUALIZATION": "VIZ_",
    "DATA_ENGINEERING": "DE_",
    "DSML": "DSML_",
    "SOURCES": "SOURCE_",
    "META": "META_",
}


def count_files_by_prefix(directory, prefix):
    count = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if (
                filename.startswith(prefix)
                or filename.startswith(f"CONCEPT_{prefix}")
                or filename.startswith(f"ENTITY_{prefix}")
            ):
                count += 1
    return count


def collect_stats():
    stats_counts = {}
    total_atomic = 0
    for category, prefix in CATEGORIES.items():
        count = count_files_by_prefix(WIKI_DIR, prefix)
        stats_counts[category] = count
        if category != "SOURCES":
            total_atomic += count
    return stats_counts, total_atomic


def scan_wiki():
    print("--- WIKI INGEST SCAN ---")
    stats_counts, total_atomic = collect_stats()

    print(f"WIKI_DIR: {WIKI_DIR}")
    print(f"INDEX_PATH: {INDEX_PATH}")
    print(f"OVERVIEW_PATH: {OVERVIEW_PATH}")
    print("")
    for category in [
        "META",
        "THINK",
        "STATS",
        "SQL",
        "PYTHON",
        "VISUALIZATION",
        "DATA_ENGINEERING",
        "DSML",
        "SOURCES",
    ]:
        print(f"{category}: {stats_counts[category]}")
    print("")
    print(f"TOTAL_ATOMIC: {total_atomic}")
    print("NEXT: Review raw source, index, and templates before writing any wiki files.")


def update_overview():
    if not os.path.exists(OVERVIEW_PATH):
        print(f"Bo qua cap nhat Overview: Khong tim thay {OVERVIEW_PATH}")
        return

    with open(OVERVIEW_PATH, "r", encoding="utf-8") as handle:
        content = handle.read()

    today = datetime.date.today().strftime("%Y-%m-%d")
    content = re.sub(r'last_updated: ".*?"', f'last_updated: "{today}"', content)

    stats_counts, total_atomic = collect_stats()
    content = re.sub(
        r"bao g.om \*\*.*?\d+ trang tri th.c nguy.n t.\*\*",
        f"bao gồm **{total_atomic} trang tri thức nguyên tử**",
        content,
    )

    table_map = {
        "THINK": "Thinking",
        "STATS": "Stats",
        "SQL": "SQL",
        "PYTHON": "Python",
        "VISUALIZATION": "Visualization",
        "DATA_ENGINEERING": "Data Engineering",
        "DSML": "DSML",
        "SOURCES": "Sources",
        "META": "Meta",
    }

    for category, label in table_map.items():
        pattern = rf"(\| \*\*.*?{label}\*\* \| )\s*~?\d+\s*( \| .*? \|)"
        if re.search(pattern, content):
            content = re.sub(pattern, rf"\1 {stats_counts[category]} \2", content)
        else:
            print(f"Canh bao: Khong tim thay hang cho {label} trong Overview.")

    content = re.sub(
        r"\*C.p nh.t l.n cu.i b.i @pm v.o \d{4}-\d{2}-\d{2}",
        f"*Cập nhật lần cuối bởi @pm vào {today}",
        content,
    )

    with open(OVERVIEW_PATH, "w", encoding="utf-8") as handle:
        handle.write(content)
    print(f"--- Da cap nhat thong ke vao {OVERVIEW_PATH} thanh cong. ---")


def update_index():
    print("--- UPDATING INDEX ---")
    try:
        script_path = os.path.join(REPO_ROOT, "scripts", "update_wiki_index.py")
        subprocess.run([sys.executable, script_path], check=True)
        print("Da cap nhat index.md bang script chuan cua repo.")
    except Exception as exc:
        print(f"Loi cap nhat index: {exc}")


def run_qmd():
    print("--- RUNNING QMD EMBED ---")
    try:
        qmd_exe = shutil.which("qmd") or shutil.which("qmd.exe")
        if not qmd_exe:
            print("Bo qua QMD embed: khong tim thay qmd trong PATH.")
            return
        subprocess.run([qmd_exe, "embed", "--collection", "wiki", "--path", WIKI_DIR], check=True)
        print("Da cap nhat Vector Embeddings thanh cong.")
    except Exception as exc:
        print(f"Loi chay QMD: {exc}")


if __name__ == "__main__":
    if "--scan" in sys.argv:
        scan_wiki()
    elif "--finalize" in sys.argv:
        update_index()
        update_overview()
        run_qmd()
    else:
        print("Su dung: python script.py --scan | --finalize")
