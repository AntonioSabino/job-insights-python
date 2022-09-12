import pytest
from src.counter import count_ocurrences


def test_counter():
    count_javascript = count_ocurrences("src/jobs.csv", "javaScript")
    assert count_javascript == 122

    count_python = count_ocurrences("src/jobs.csv", "PYTHON")
    assert count_python == 1639

    with pytest.raises(FileNotFoundError):
        count_ocurrences("src/jobs.cs", "javaScript")
