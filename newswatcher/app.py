import logging
from flask import Flask
from newswatcher.database import mgdb
# from newswatcher.extensions import kafka_producer, kafka_consumer

logger = logging.getLogger(__name__)


def create_app(config_object):

    app = Flask(__name__)
    app.config.from_object(config_object)

    register_database(app)
    # register_extensions(app)
    register_blueprints(app)

    logger.info(app.url_map)
    return app


def register_database(app):
    mgdb.init_app(app)


# def register_extensions(app):
#     mgdb.init_app(app)


def register_blueprints(app):

    import newswatcher.crawler.views as crawler_views
    import newswatcher.storage.mongo.store as storage_mongo_store

    app.register_blueprint(crawler_views.blueprint, url_prefix='')
    app.register_blueprint(storage_mongo_store.blueprint, url_prefix='')

    logger.info(app.url_map)
