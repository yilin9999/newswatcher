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
        "ETtoday"
        # "TVBS新聞",
        # "台灣蘋果日報",
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
        # news_cnt += len(results)

        for i in range(1, 2):
            print("Get page {}".format(i))
            news_cnt = NewsDoc.count_doc()

            google_news_search = GoogleNewsSearch(query=query, start_date="5/15/2020", result_per_page=50)
            google_news_search.getpage(page=i, delay=2)
            results = google_news_search.result()

            if len(results) == 0:
                break

            try:
                NewsDoc.insert_many(results, ordered=False)
            except pymongo.errors.BulkWriteError as e:
                logging.info(str(e))
            except Exception as e:
                logging.error(str(e))

            news_inc = NewsDoc.count_doc() - news_cnt
            print("--> find news: {}".format(news_inc))

    return "OK", 200, {'Content-Type': 'application/json; charset=utf-8'}

# https://www.google.com/search?q=%E6%96%B0%E8%81%9E&safe=active&rlz=1C5CHFA_enTW890TW890&tbm=nws&sxsrf=ALeKk01MGEVHB_-45xPSree2A1wE8ytxkA:1591525190057&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwj0v-qsve_pAhVnxosBHR4gDCAQpwUIJA&biw=1920&bih=945&dpr=1
# https://www.google.com/search?q=%E6%96%B0%E8%81%9E&safe=active&rlz=1C5CHFA_enTW890TW890&sxsrf=ALeKk02GXt7JvLS8BoY8NW7rvTf3Mw_VFw:1591525188675&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiPkJasve_pAhWBF6YKHazbCMEQ_AUoAXoECBMQAw&biw=1920&bih=945
#https://www.google.com/search?q=ETtoday&safe=active&rlz=1C5CHFA_enTW890TW890&biw=1920&bih=945&sxsrf=ALeKk03gNTayBDdAwd-OuDqXmLOVgBBlCg%3A1591526191881&source=lnt&tbs=cdr%3A1%2Ccd_min%3A6%2F1%2F2020%2Ccd_max%3A6%2F2%2F2020&tbm=nws
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
