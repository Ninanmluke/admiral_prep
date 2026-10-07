from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))

from analysis.ae_summary import load_records, summarize_adverse_events


class AdverseEventSummaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.records = load_records(ROOT / "data" / "synthetic_adae.csv")
        cls.summary = summarize_adverse_events(cls.records)

    def test_includes_two_severe_events(self) -> None:
        self.assertEqual(len(self.summary), 2)

    def test_contains_only_severe_events(self) -> None:
        self.assertEqual({record["AESEV"] for record in self.summary}, {"SEVERE"})

    def test_preserves_output_columns(self) -> None:
        self.assertTrue(self.summary)
        self.assertEqual(
            tuple(self.summary[0]),
            ("USUBJID", "AETERM", "AESEV"),
        )


if __name__ == "__main__":
    unittest.main()
