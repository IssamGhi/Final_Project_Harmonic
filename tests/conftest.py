import pytest

from utils.app_factory import create_app


@pytest.fixture(scope='session')
def get_app():
    return create_app({'MODE': 'TEST'})


@pytest.fixture(scope='session')
def user(get_app):
    # get_app.testing = True  # We use this if we are testing for exceptions
    with get_app.test_client() as u:
        yield u


@pytest.fixture(scope='session')
def get_jwt(user):
    response = user.post('/users/login', json={'email': 'metelyk@db', 'password': '123'})
    return response.json
