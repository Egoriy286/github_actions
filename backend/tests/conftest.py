import pytest

from app import app


@pytest.fixture
def test_app():
    app.config["TESTING"] = True
    yield app


@pytest.fixture
def client(test_app):
    return test_app.test_client()
