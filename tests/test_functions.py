from lib import chunks, sliding_window
from tests import generated as mocks
import os
import numpy as np

# copy test dataset file to string
filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "dataset.txt"))
with open(filepath, "r") as fin:
    dataset = fin.read()

# test the functions


def test_make_chunks():
    lst = ["a", "b", "c", "d"]
    expected = [["a", "b"], ["c", "d"]]
    chunked = chunks.make_chunks(lst, 2)
    np.array_equal(np.array(chunked), np.array(expected))


def test_chunkit():
    str = "I know chicken math"
    expected = [["I", "know"], ["chicken", "math"]]
    chunked = chunks.chunkit(str, 2)
    np.array_equal(np.array(chunked), np.array(expected))


def test_unique():
    duplicates = chunks.run(3, mocks.unique, dataset)
    assert len(duplicates) == 0


def test_series6():
    dupecheck_found(mocks.duplicate_series6, mocks.duplicate_series6_common, dataset)


def dupecheck_found(text, expected, data):
    duplicates = chunks.dupecheck(min=3, max=12, text=text, dataset=data, verbose=True)
    assert len(duplicates) > 0
    # assert duplicates[0] == text


def sliding_window_run(window_length, text, expected, data):
    duplicates = sliding_window.run(window_length, text, data)
    assert len(duplicates) > 0


def test_sw_run_series3():
    sliding_window_run(
        3, mocks.duplicate_series3, mocks.duplicate_series3_common, dataset
    )


def test_sw_run_series4():
    sliding_window_run(
        4, mocks.duplicate_series4, mocks.duplicate_series4_common, dataset
    )


def test_sw_run_series5():
    sliding_window_run(
        5, mocks.duplicate_series5, mocks.duplicate_series5_common, dataset
    )


def test_sw_run_series6():
    sliding_window_run(
        6, mocks.duplicate_series6, mocks.duplicate_series6_common, dataset
    )


def sw_dupecheck(min, text, expected, data):
    duplicates = sliding_window.dupecheck(
        min=min, max=12, text=text, dataset=data, verbose=True
    )
    assert len(duplicates) > 0
    assert expected in duplicates


def test_sw_dupecheck_series3():
    sw_dupecheck(3, mocks.duplicate_series3, mocks.duplicate_series3_common, dataset)


def test_sw_dupecheck_series4():
    sw_dupecheck(4, mocks.duplicate_series4, mocks.duplicate_series4_common, dataset)


def test_sw_dupecheck_series5():
    sw_dupecheck(5, mocks.duplicate_series5, mocks.duplicate_series5_common, dataset)


def test_sw_dupecheck_series6():
    sw_dupecheck(6, mocks.duplicate_series6, mocks.duplicate_series6_common, dataset)
