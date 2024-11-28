from pathlib import Path
import pytest
from pact import Consumer, Provider, Verifier
from yarl import URL
from taf.consumer import BookClient


@pytest.fixture(scope='session')
def mock_url():
    return URL("http://localhost:8080")


@pytest.fixture(scope='session')
def pact_dir():
    return Path(__file__).parent


@pytest.fixture(scope='session')
def pact_artifacts_dir(pact_dir):
    return pact_dir / 'pact_artifacts'


@pytest.fixture(scope='session')
def books_client(mock_url):
    return BookClient(str(mock_url))


@pytest.fixture(scope='module')
def books_pact(mock_url, pact_artifacts_dir):
    consumer = Consumer("BookConsumer")
    pact = consumer.has_pact_with(
        Provider("BookProvider"),
        pact_dir=str(pact_artifacts_dir),
        log_dir=str(pact_artifacts_dir),
        host_name=mock_url.host,
        port=mock_url.port,
    )
    pact.start_service()
    yield pact
    pact.stop_service()


@pytest.fixture(scope="module")
def verifier(provider_url):
    verifier = Verifier(
        provider="BookProvider",
        provider_base_url=str(provider_url),
    )
    yield verifier
