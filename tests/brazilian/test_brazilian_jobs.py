import pytest
from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    brazilian_jobs_list = read_brazilian_file(
        "tests/mocks/brazilians_jobs.csv"
    )

    for job in brazilian_jobs_list:
        assert "title" in job.keys()
        assert "salary" in job.keys()
        assert "type" in job.keys()

    with pytest.raises(FileNotFoundError):
        read_brazilian_file("tests/mocks/argentinians_jobs")
