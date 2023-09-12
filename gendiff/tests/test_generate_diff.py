from gendiff import generate_diff
import pytest


@pytest.fixtures
def 
def test_generate_diff(file1, file2, expected_filename):
    with open(expected_filename, "r") as expected_file:
        assert expected_file.read() == generate_diff(file1, file2)
