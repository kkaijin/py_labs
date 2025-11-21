import pytest
import sys
import os

sys.path.append("/Applications/Python_3.13/proga/py_labs/src/lab_05")
from json_csv import *


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    # TODO: Реализовать тесты для конвертации в другую сторону
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    data = "name,age\nAlice,22\nBob,25\n"

    src.write_text(data, encoding="utf-8")

    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        result = json.load(f)

    assert len(result) == 2
    assert result[0]["name"] == "Alice"
    assert result[1]["age"] == "25"
