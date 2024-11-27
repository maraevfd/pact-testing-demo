import pytest
from pact import Consumer, Provider
from taf.consumer import BookClient


@pytest.fixture(scope='session')
def books_pact():
    consumer = Consumer("BookConsumer")
    pact = consumer.has_pact_with(
        Provider("BookProvider"),
    )
    pact.start_service()
    yield pact
    pact.stop_service()


@pytest.fixture(scope='session')
def books_client(books_pact):
    return BookClient(books_pact.uri)
