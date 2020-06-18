import pytest
from newswatcher.app import create_app
from newswatcher.settings import AppConfig


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    app = create_app(AppConfig)
    app.config['TESTING'] = True
    app.config['JSON_AS_ASCII'] = False
    # with app.app_context():
    #     db.create_all()
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    client = app.test_client()

    # Establish an application context before running the tests.
    # for SQLAlchemy setting
    ctx = app.app_context()
    # ctx = app.test_request_context()
    ctx.push()

    yield client  # this is where the testing happens!

    ctx.pop()

# @pytest.fixture(scope='module')
# def test_app():

#     _app = create_app(AppConfig)

#     # with _app.app_context():
#     #     db.create_all()

#     ctx = _app.test_request_context()
#     ctx.push()
#     yield _app
#     ctx.pop()
