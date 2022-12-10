import pytest
from loguru import logger

@pytest.fixture()
def sample_fixture():
    logger.info("Set Up method is called...!!")
    yield ''
    logger.info("Tear Down Method is called...!!")

def test_fixture(sample_fixture):
    logger.info("Test Method is called...!!")
