from django.test import Client
import pytest
import os
from django.conf import settings
import yaml
from yaml.loader import SafeLoader

file_path = os.path.dirname(os.path.abspath(__file__))
test_data_files = [file for file in os.listdir(file_path) if '.yaml' in file]

# authorisation_payload = {
#     "username": "my name is apple",
#     "email": "apple@gail.com",
#     "useremail": "apple@gmail.com",
#     "password": "2222",
#     "password2": "2222",
#     "first_name": "",
#     "last_name": "",
#     "qahub_user": "",
#     "access_roles": ""}

def pytest_addoption(parser):
    """Method to add the option to ini."""
    parser.addoption('--execute_all', action="store", default=True)
    parser.addoption('--execute_endpoint', action="store", default='all')
    parser.addoption('--filename', action="store", default='all')
    parser.addoption('--env', action="store", default='local')


@pytest.fixture(scope='session', autouse=True)
def django_db_setup():
    pass

# @pytest.fixture(autouse=True)
# def set_up(django_db_setup, request, pytestconfig):
#     server = Client()
#     payload = authorisation_payload
#     authorisation_token = server.post('/register_user/',
#                                       data=payload).json()['access']
#     request.module.server = server
#     request.module.auth_token = 'Bearer {}'.format(authorisation_token)
#     yield server

@pytest.fixture(autouse=True)
def set_up(django_db_setup, request, pytestconfig):
    server = Client()
    request.module.server = server
    yield server


def pytest_generate_tests(metafunc):
    parameterised_data, data = [], {}
    execute_all = metafunc.config.getoption('--execute_all')
    default_end_point = metafunc.config.getoption('--execute_endpoint')
    default_file = metafunc.config.getoption('--filename')
    # Load Data From Yaml Files
    for file in test_data_files:
        if file in default_file or 'all' in default_file:
            with open(file_path + '/' + file, 'r') as f:
                data.update(list(yaml.load_all(f, Loader=SafeLoader))[0])
    # Generating Tests Based on test data provided
    for each_end_point in data:
        end_point = data[each_end_point]['end_point']
        if each_end_point == default_end_point or str(
                execute_all).lower() == 'true':
            request_method = data[each_end_point]['method']
            for payload in data[each_end_point]['payload']:
                expected_data = payload['expected_data']
                formdata = payload['formdata'] if 'formdata' \
                    in payload.keys() else payload
                content_type = payload['content_type'] if 'content_type' \
                    in payload.keys() else ''
                del payload['expected_data']
                try:
                    del payload['formdata']   
                except:
                    pass
                try:
                    del payload['content_type']
                except:
                    pass
                parameterised_data.append((end_point,
                                           payload,
                                           request_method,
                                           formdata,
                                           content_type,
                                           expected_data))
    metafunc.parametrize("end_point,payload,request_method,formdata, \
        content_type,expected_data", parameterised_data)
