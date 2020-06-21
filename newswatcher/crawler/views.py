import logging
from time import monotonic as timer
# import pymongo
import json
import datetime as dt
from flask import request, Blueprint
from flask import jsonify
from newswatcher.settings import AppConfig
from newswatcher.extensions import kafka_producer, KafkaQueueItem
from .ggsearch import GoogleNewsSearch
from .schema import GsearchConfigSchema

logger = logging.getLogger(__name__)
blueprint = Blueprint('crawler', __name__)


# @blueprint.route('/news', methods=('POST',))
@blueprint.route('/crawler', methods=('POST',))
def crawler_search_news():
    rsp_dict = {}
    try:
        data_raw = request.data.decode('utf-8')
        gsearch_schema = GsearchConfigSchema()
        body_dict = gsearch_schema.load(json.loads(data_raw))
    except Exception as e:
        logging.error(e)
        rsp_dict['msg'] = str(e)
        rsp_code = 400

    for query in body_dict['queries']:
        for i in range(1, 2):
            logger.info("[{}] Get page {}".format(query, i))
            start_t = timer()
            google_news_search = GoogleNewsSearch(
                                    query=query,
                                    start_date=body_dict["start_date"].strftime("%m/%d/%Y"),
                                    end_date=body_dict["end_date"].strftime("%m/%d/%Y"),
                                    result_per_page=50)
            google_news_search.getpage(page=i, delay=2)
            results = google_news_search.result()
            if len(results) == 0:
                break

            time_elapsed = round(timer() - start_t, 2)
            queue_item = KafkaQueueItem(
                            body=results,
                            time_elapsed=time_elapsed)
            kafka_producer.send(AppConfig.KAFKA_TOPIC_MONGODB, queue_item.items)
            kafka_producer.flush()
            logger.info("--> find news: {} time_elapsed: {}".format(queue_item.items['data_cnt'], time_elapsed))

    rsp_dict['job_uid'] = "test"
    rsp_dict['created_at'] = dt.datetime.utcnow()
    rsp_code = 200

    # jsonify will aitomatically set Content-Type': 'application/json
    return jsonify(rsp_dict), rsp_code

    # return "OK", 200, {'Content-Type': 'application/json; charset=utf-8'}

# https://www.google.com/search?q=%E6%96%B0%E8%81%9E&safe=active&rlz=1C5CHFA_enTW890TW890&tbm=nws&sxsrf=ALeKk01MGEVHB_-45xPSree2A1wE8ytxkA:1591525190057&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwj0v-qsve_pAhVnxosBHR4gDCAQpwUIJA&biw=1920&bih=945&dpr=1
# https://www.google.com/search?q=%E6%96%B0%E8%81%9E&safe=active&rlz=1C5CHFA_enTW890TW890&sxsrf=ALeKk02GXt7JvLS8BoY8NW7rvTf3Mw_VFw:1591525188675&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiPkJasve_pAhWBF6YKHazbCMEQ_AUoAXoECBMQAw&biw=1920&bih=945
# https://www.google.com/search?q=ETtoday&safe=active&rlz=1C5CHFA_enTW890TW890&biw=1920&bih=945&sxsrf=ALeKk03gNTayBDdAwd-OuDqXmLOVgBBlCg%3A1591526191881&source=lnt&tbs=cdr%3A1%2Ccd_min%3A6%2F1%2F2020%2Ccd_max%3A6%2F2%2F2020&tbm=nws
# https://www.google.com/search?q=%E6%96%B0%E8%81%9E&safe=active&rlz=1C5CHFA_enTW890TW890&sxsrf=ALeKk02GXt7JvLS8BoY8NW7rvTf3Mw_VFw:1591525188675&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiPkJasve_pAhWBF6YKHazbCMEQ_AUoAXoECBMQAw
# https://www.google.com/search?q=%E6%96%B0%E8%81%9E&safe=active&rlz=1C5CHFA_enTW890TW890&tbm=nws&sxsrf=ALeKk02c3a5EJaaVApJNeCb3VvPFQ95PnA:1591525249365&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwiQp47Jve_pAhUKzIsBHc4ODa8QpwUIJA&biw=1920&bih=945&dpr=1
# import time
# from ggsearch import GoogleNewsSearch
# from elasticsearch import Elasticsearch
# from elasticsearch import helpers
# from pymongo import MongoClient

# es = Elasticsearch()


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         print('runtime: {:.2f} sec'.format(time.time() - start))
#         return res
#     return wrapper


# @timer
# def create_data():
#     for line in range(100):
#         es.index(index='s2', doc_type='doc', body={'title': line})


# def connect_mongo():
#     uri = "mongodb://david:newsgogogo@localhost?authSource=source"
#     client = MongoClient(uri)
#     db = client['news']


# def start():

#     #google_news_search = GoogleNewsSearch(query="報導者")
#     #create_data()
#     connect_mongo()



#     # for i in range(1, 2):
#     #     google_news_search.getpage(i)
#     #     result = google_news_search.result()
#     #     print(result)
#     #     time.sleep(2)

# # @classmethod
# # @timer
# # def batch_data(input_dict):
# #     """ 批量写入数据 """
# #     action = {
# #         "_index": "s2",
# #         "_type": "doc",
# #         "_source": input_dict
# #     }
# #     helpers.bulk(es, action)
