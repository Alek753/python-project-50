from gendiff.generate_diff import generate_diff
import pytest
import os


FIXTURES_PATH = f'{os.path.dirname(__file__)}/fixtures'


@pytest.mark.parametrize("file1, file2, expected_filename", [
    (
        f'{FIXTURES_PATH}/example_file1.json',
        f'{FIXTURES_PATH}/example_file2.json',
        f'{FIXTURES_PATH}/expected_for_examples.txt'
    ),
    (
        f'{FIXTURES_PATH}/example_file1.yml',
        f'{FIXTURES_PATH}/example_file2.yml',
        f'{FIXTURES_PATH}/expected_for_examples.txt'
    ),
    (
        f'{FIXTURES_PATH}/file1.json',
        f'{FIXTURES_PATH}/file2.json',
        f'{FIXTURES_PATH}/expected_for_stylish.txt'
    ),])
def test_generate_diff(file1, file2, expected_filename):
    with open(expected_filename, "r") as expected_file:
        assert expected_file.read() == generate_diff(file1, file2)
