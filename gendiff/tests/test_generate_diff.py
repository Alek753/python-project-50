from generate_diff import generate_diff
import pytest
import os


FIXTURES_PATH = f'{os.path.dirname(__file__)}/fixtures'


@pytest.fixture
def example_parameters():
    file1 = f'{FIXTURES_PATH}/file1.json'
    file2 = f'{FIXTURES_PATH}/file2.json'
    return file1, file2


@pytest.fixture
def expected_parameter():
    expected_filename = f'{FIXTURES_PATH}/expected_for_examples.txt'
    return expected_filename


def test_generate_diff(example_parameters, expected_parameter):
    with open(expected_parameter, "r") as expected_file:
        file1, file2 = example_parameters
        assert expected_file.read() == generate_diff(file1, file2)
