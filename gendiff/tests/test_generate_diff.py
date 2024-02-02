from gendiff.generate_diff import generate_diff
import pytest
import os


FIXTURES_PATH = f'{os.path.dirname(__file__)}/fixtures'


@pytest.mark.parametrize("file1, file2, expected_filename, format", [
    (
        f'{FIXTURES_PATH}/file1.json',
        f'{FIXTURES_PATH}/file2.json',
        f'{FIXTURES_PATH}/expected_for_plain.txt',
        "plain"
    ),
    (
        f'{FIXTURES_PATH}/file1.yml',
        f'{FIXTURES_PATH}/file2.yml',
        f'{FIXTURES_PATH}/expected_for_plain.txt',
        "plain"
    ),
    (
        f'{FIXTURES_PATH}/example_file1.json',
        f'{FIXTURES_PATH}/example_file2.json',
        f'{FIXTURES_PATH}/expected_for_examples.txt',
        "stylish"
    ),
    (
        f'{FIXTURES_PATH}/example_file1.yml',
        f'{FIXTURES_PATH}/example_file2.yml',
        f'{FIXTURES_PATH}/expected_for_examples.txt',
        "stylish"
    ),
    (
        f'{FIXTURES_PATH}/file1.json',
        f'{FIXTURES_PATH}/file2.json',
        f'{FIXTURES_PATH}/expected_for_stylish.txt',
        "stylish"
    ),
    (
        f'{FIXTURES_PATH}/file1.yml',
        f'{FIXTURES_PATH}/file2.yml',
        f'{FIXTURES_PATH}/expected_for_stylish.txt',
        "stylish"
    ),])
def test_generate_diff(file1, file2, expected_filename, format):
    with open(expected_filename, "r") as expected_file:
        assert expected_file.read() == generate_diff(file1, file2, format)
