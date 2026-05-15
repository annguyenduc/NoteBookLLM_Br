import pathlib
import shutil
import subprocess
import tempfile
import unittest
import sys


SCRIPT = pathlib.Path("scripts/maintenance/ingest_lifecycle_check.py").resolve()


def _write_report(path: pathlib.Path, body: str) -> None:
    path.write_text(body, encoding="utf-8")


class TestIngestLifecycleCheck(unittest.TestCase):
    def setUp(self):
        self.temp_dir = pathlib.Path(tempfile.mkdtemp(prefix="ingest_lifecycle_test_", dir="scratch"))

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _run(self, *args):
        cmd = [sys.executable, str(SCRIPT), *args]
        return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    def test_happy_path_done(self):
        prep = self.temp_dir / "prep.md"
        audit = self.temp_dir / "audit.md"
        lock = self.temp_dir / "lock.md"
        orch = self.temp_dir / "orch.md"
        gen = self.temp_dir / "gen.md"
        close = self.temp_dir / "close.md"

        _write_report(prep, 'SOURCE PREP REPORT:\nsource_evidence_file: "a.pdf"\nstaging_status: "READY"\n')
        _write_report(audit, 'SOURCE AUDIT REPORT:\nsource_evidence_file: "a.pdf"\npromoted_artifact: "a.md"\naudit_status: "PASSED"\nready_for_input_lock: "YES"\n')
        _write_report(lock, 'INGEST INPUT LOCK:\nsource_evidence_file: "a.pdf"\nprimary_ingest_file: "a.md"\nsource_id: "A"\nstatus: "READY"\n')
        _write_report(orch, 'INGEST ORCHESTRATION REPORT:\nsource_id: "A"\nstatus: "READY_FOR_GENERATE"\n')
        _write_report(gen, 'INGEST GENERATE REPORT:\nsource_id: "A"\nstatus: "DONE"\n')
        _write_report(close, 'INGEST CLOSEOUT REPORT:\nsource_id: "A"\nstatus: "DONE"\n')

        result = self._run("--source-prep", str(prep), "--source-audit", str(audit), "--input-lock", str(lock), "--orchestration", str(orch), "--generate", str(gen), "--closeout", str(close))
        self.assertEqual(result.returncode, 0)
        self.assertIn('next_stage: "DONE"', result.stdout)
        self.assertIn('lifecycle_status: "DONE"', result.stdout)

    def test_blocked_path_at_audit(self):
        prep = self.temp_dir / "prep.md"
        audit = self.temp_dir / "audit.md"

        _write_report(prep, 'SOURCE PREP REPORT:\nsource_evidence_file: "a.pdf"\nstaging_status: "READY"\n')
        _write_report(audit, 'SOURCE AUDIT REPORT:\nsource_evidence_file: "a.pdf"\npromoted_artifact: "a.md"\naudit_status: "FAILED"\nready_for_input_lock: "NO"\n')

        result = self._run("--source-prep", str(prep), "--source-audit", str(audit))
        self.assertEqual(result.returncode, 1)
        self.assertIn('next_stage: "audit-promote-source"', result.stdout)
        self.assertIn('lifecycle_status: "BLOCKED"', result.stdout)

    def test_resume_path_to_ingest(self):
        prep = self.temp_dir / "prep.md"
        audit = self.temp_dir / "audit.md"
        lock = self.temp_dir / "lock.md"

        _write_report(prep, 'SOURCE PREP REPORT:\nsource_evidence_file: "a.pdf"\nstaging_status: "READY"\n')
        _write_report(audit, 'SOURCE AUDIT REPORT:\nsource_evidence_file: "a.pdf"\npromoted_artifact: "a.md"\naudit_status: "PASSED"\nready_for_input_lock: "YES"\n')
        _write_report(lock, 'INGEST INPUT LOCK:\nsource_evidence_file: "a.pdf"\nprimary_ingest_file: "a.md"\nsource_id: "A"\nstatus: "READY"\n')

        result = self._run("--source-prep", str(prep), "--source-audit", str(audit), "--input-lock", str(lock))
        self.assertEqual(result.returncode, 0)
        self.assertIn('current_stage: "lock-ingest-input"', result.stdout)
        self.assertIn('next_stage: "ingest"', result.stdout)
        self.assertIn('lifecycle_status: "IN_PROGRESS"', result.stdout)


if __name__ == "__main__":
    unittest.main()
