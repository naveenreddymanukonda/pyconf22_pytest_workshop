import pytest
from loguru import logger

@pytest.fixture(scope='function')
def function_fixture():
    print('Set Up function in <function scope is called...!!>')
    yield
    print('Tear Down function in <function scope is called...!!>')


@pytest.fixture(scope='module')
def module_fixture():
    print('Set Up function in <Module scope is called...!!>')
    yield
    print('Tear Down function in <Module scope is called...!!>')


@pytest.mark.parametrize('a', range(3))
def test_sample(module_fixture, function_fixture, a):
    print(a)

   
