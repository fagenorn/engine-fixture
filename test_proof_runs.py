import unittest
from pathlib import Path

LOG = Path(__file__).resolve().parent / "proof-runs.log"


class Issue2ProofRunLogTest(unittest.TestCase):
    def test_log_holds_issue_2_line(self) -> None:
        lines = LOG.read_text(encoding="utf-8").splitlines()
        self.assertIn("issue 2", lines)


if __name__ == "__main__":
    unittest.main()
