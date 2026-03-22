"""Example showing reading/writing CSV using the standard library."""
import csv
from pathlib import Path

SAMPLE_CSV = Path("sample_data.csv")


def create_sample(path: Path):
    rows = [
        ["id", "name", "score"],
        [1, "Alice", 85],
        [2, "Bob", 92],
        [3, "Charlie", 78],
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def read_csv(path: Path):
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


if __name__ == "__main__":
    if not SAMPLE_CSV.exists():
        print("Creating sample CSV:", SAMPLE_CSV)
        create_sample(SAMPLE_CSV)
    data = read_csv(SAMPLE_CSV)
    print("Rows:")
    for row in data:
        print(row)
