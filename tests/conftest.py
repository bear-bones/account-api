import os
import pytest

from app import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })

    yield app


@pytest.fixture
def client():
    return app.test_client()

@pytest.fixture
def runner():
    return app.test_cli_runner()
