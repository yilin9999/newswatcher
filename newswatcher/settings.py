import os
from dotenv import load_dotenv

load_dotenv()
curr_stage = os.getenv('STAGE', default=None)


class Config(object):
    TEST = ''


class ProdConfig(Config):
    STAGE = 'production'


class DevConfig(Config):
    STAGE = 'dev'
    MONGO_URI = 'mongodb://david:newsgogogo@localhost:27017/newswatcher'
    TESTING = True
    KAFKA_TOPIC_MONGODB = 'test_mongodb'
    # DBNAME = 'newswatcher'
    # MONGODB_SETTINGS = {
    #     'db': 'newswatcher',
    #     'host': 'mongodb://localhost:27017/newswatcher'
    #     # 'host': 'localhost',
    #     # 'port': 27017,
    #     # 'username': 'david',
    #     # 'password': 'newsgogogo'
    # }


if curr_stage == 'production':
    AppConfig = ProdConfig
else:
    AppConfig = DevConfig
