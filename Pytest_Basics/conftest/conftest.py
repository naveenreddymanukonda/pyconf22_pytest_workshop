import pytest

# def pytest_generate_tests(metafunc):
#     metafunc.parametrize("num1, num2, output", ([2, 2, 4], [3, 7, 10], [48, 52, 100]))
def pytest_addoption(parser):
    """Method to add the option to ini."""
    parser.addoption('--test_data', action="store", default='Test')

@pytest.fixture()
def sample_fixture(request, pytestconfig):
    test_data = pytestconfig.getoption('--test_data').lower()
    yield test_data



   
