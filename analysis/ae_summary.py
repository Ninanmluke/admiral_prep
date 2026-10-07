"""Create the synthetic adverse-event summary for requirement AE-3."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

OUTPUT_COLUMNS = ("USUBJID", "AETERM", "AESEV")


def load_records(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def summarize_adverse_events(
    records: Iterable[dict[str, str]],
) -> list[dict[str, str]]:
    return [
        {column: record[column] for column in OUTPUT_COLUMNS}
        for record in records
        if record["AESEV"] == "SEVERE"
    ]


def main() -> None:
    data_path = Path(__file__).parents[1] / "data" / "synthetic_adae.csv"
    for record in summarize_adverse_events(load_records(data_path)):
        print(",".join(record[column] for column in OUTPUT_COLUMNS))


if __name__ == "__main__":
    main()
