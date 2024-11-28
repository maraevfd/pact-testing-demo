import pytest
from yarl import URL


@pytest.fixture(scope='session')
def provider_url():
    return URL("http://localhost:8080")
