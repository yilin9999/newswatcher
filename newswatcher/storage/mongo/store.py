import logging
from pymongo.errors import BulkWriteError
from flask import request, Blueprint
from flask import make_response
from marshmallow import ValidationError
from .models import NewsMongoDoc
from newswatcher.schema import NewsSchema

logger = logging.getLogger(__name__)
blueprint = Blueprint('storage/mongo', __name__)


@blueprint.route('/storage/mongo', methods=('POST',))
def store_into_mongo():
    body_raw = request.data.decode('utf-8')
    news_schema = NewsSchema()
    try:
        body_dict = news_schema.loads(body_raw)
        logger.debug(body_dict)
    except ValidationError as e:
        logger.error(e)
        return make_response(str(e), 422)

    try:
        news_cnt = NewsMongoDoc.count_doc()
        NewsMongoDoc.insert_many(body_dict['data'], ordered=False)
    except BulkWriteError as e:
        logging.error(str(e))
    except Exception as e:
        logging.error(str(e))
        news_cnt = NewsMongoDoc.count_doc()
    news_inc = NewsMongoDoc.count_doc() - news_cnt
    return make_response("Created ({})".format(news_inc), 201)
