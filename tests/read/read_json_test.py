from pytest import mark, raises

from environment_variables.read import read_json


def test_when_read_json_with_valid_file_path_must_return_data():
    data_return = read_json(file_path='tests/environment_test_files/test.json')

    expected_return = [
        {
            "key": 1,
            "value": 1
        },
        {
            "key": 2,
            "value": 3
        }
    ]
    assert data_return == expected_return
