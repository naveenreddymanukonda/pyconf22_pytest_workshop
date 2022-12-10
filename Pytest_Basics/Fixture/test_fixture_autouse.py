import pytest
from loguru import logger

@pytest.fixture(autouse=True) # By default autouse is setting to False
def sample_fixture():
    logger.info("Set Up method is called...!!")
    yield ''
    logger.info("Tear Down Method is called...!!")

def test_fixture():
    logger.info("Test Method is called...!!")
