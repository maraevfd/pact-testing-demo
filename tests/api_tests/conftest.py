import pytest
from taf.consumer import BookClient


@pytest.fixture(scope='session')
def book_client():
    return BookClient()