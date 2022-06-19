from pytest import mark, raises

from environment_variables.read import read_json


def test_when_read_json_with_normal_data_must_return_data():
    data_return = read_json(file_path='tests/environment_test_files/test.json')

    expected_return = {
        "key1": 1,
        "key2": 2
    }

    assert data_return == expected_return
