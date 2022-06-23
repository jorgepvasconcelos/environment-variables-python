from environment_variables.read import read_yaml


def test_when_read_yaml_with_normal_data_must_return_data():
    data_return = read_yaml(file_path='tests/environment_test_files/test.yaml')

    expected_return = {'PRD': {'DB_HOST': 'url_prd', 'PORT': 3306, 'USER': 'super', 'PASSWORD': 123},
                       'HML': {'DB_HOST': 'url_hml', 'PORT': 3306, 'USER': 'super_hml', 'PASSWORD': 123}}

    assert data_return == expected_return
