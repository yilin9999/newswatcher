import logging
from flask import Flask
from newswatcher.database import mgdb

logger = logging.getLogger(__name__)


def create_app(config_object):

    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)

    logger.info(app.url_map)
    return app


def register_extensions(app):

    mgdb.init_app(app)


def register_blueprints(app):

    import newswatcher.crawler.views as crawler_views

    app.register_blueprint(crawler_views.blueprint, url_prefix='')
