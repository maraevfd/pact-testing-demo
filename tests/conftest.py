import pytest
from pact import Consumer, Provider
from taf.consumer import BookUser


@pytest.fixture(scope='session')
def book_client():
    return BookUser()

@pytest.fixture(scope='session')
def books_pact():
    pact = Consumer("BookConsumer").has_pact_with(Provider("BookProvider"))
    pact.start_service()
    yield pact
    pact.stop_service()
