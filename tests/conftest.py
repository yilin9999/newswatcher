import pytest
from newswatcher.app import create_app
from newswatcher.settings import AppConfig


@pytest.fixture(scope='module')
def test_app():

    _app = create_app(AppConfig)

    # with _app.app_context():
    #     db.create_all()

    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    ctx.pop()
