import pytest
import sys
import os

sys.path.append("/Applications/Python_3.13/proga/py_labs/src/lib")
from text import *


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\\nМИр\\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\\r\\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
    ],
)
def test_tokenize_basic(source, expected):
    # TODO: Реализовать тесты токенизации
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        (["bb", "aa", "bb", "aa", "cc"], {"aa": 2, "bb": 2, "cc": 1}),
        ([], None),
    ],
)
def test_count_freq_and_top_n(source, expected):
    # TODO: Реализовать тесты частоты
    assert count_freq(source) == expected


@pytest.mark.parametrize(
    "source, source2, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),
        ({"aa": 2, "bb": 2, "cc": 1}, 2, [("aa", 2), ("bb", 2)]),
        ({"aa": 2, "cc": 2, "bb": 2}, 2, [("aa", 2), ("bb", 2)]),
        ({}, 2, None),
    ],
)
def test_top_n_tie_breaker(source, source2, expected):
    # TODO: Реализовать тесты для топ_н
    assert top_n(source, source2) == expected
