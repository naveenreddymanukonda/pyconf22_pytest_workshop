import pytest
from loguru import logger

def pytest_generate_tests(metafunc):
    metafunc.parametrize("num1, num2, output", ([2, 2, 4], [3, 7, 10], [48, 52, 100]))





   
