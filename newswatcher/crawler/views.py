import logging
import time
import pymongo
from flask import request, Blueprint
from .ggsearch import GoogleNewsSearch
from .models import NewsDoc

logger = logging.getLogger(__name__)
blueprint = Blueprint('news', __name__)


@blueprint.route('/news', methods=('POST',))
def search_news():
    query_list = [
        "台灣蘋果日報",
        # "中時電子報",
        # "自由時報",
        # "UDN 聯合新聞網",
        # "新頭殼",
        # "風傳媒",
        # "端傳媒",
        # "三立新聞網",
        # "中央社即時新聞",
        # "Yahoo奇摩新聞",
        # "The News Lens 關鍵評論網",
        # "報導者The Reporter",
        # "Yahoo奇摩",
        # "翻爆",
        # "數位時代",
        # "經濟日報",
        # "工商時報",
        # "更生日報",
        # "世界日報"
    ]
    for query in query_list:
        print("Get news from [{}]".format(query))
        news_cnt = 0

        for i in range(1, 2):
            print("Get page {}".format(i))

            google_news_search = GoogleNewsSearch(query=query, start_date="6/1/2020", result_per_page=50)
            google_news_search.getpage(page=i, delay=2)
            results = google_news_search.result()

            if len(results) == 0:
                break

            try:
                NewsDoc.insert_many(results)
                news_cnt += len(results)
            except pymongo.errors.BulkWriteError as e:
                logging.info(str(e))
            except Exception as e:
                logging.error(str(e))

            print("--> find news: {}".format(news_cnt))

    return "OK", 200, {'Content-Type': 'application/json; charset=utf-8'}

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
