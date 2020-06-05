from newswatcher.app import create_app
from newswatcher.settings import AppConfig

app = create_app(AppConfig)


# from ggsearch.ggnews_search import GoogleNewsSearch
# google_news_search = GoogleNewsSearch()

# google_news_search = GoogleNewsSearch(keywrod=['abc'])
# print(google_news_search.__dict__)
# import googlesearch


# result = googlesearch.search_news(query="報導者", stop=1)
# #result = googlesearch.search(query="Trump", tpe='nws', stop=2)
# #print(next(result))
# r = googlesearch.get_page(next(result))
# print(r.decode())

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

# for itr in result:
#     print(itr)

# # -*- coding: utf-8 -*-
# from news.google_news_cn import GoogleNewsCN
# from GoogleNews import GoogleNews

# googlenews = GoogleNews(start='05/20/2020', end='05/26/2020')
# # googlenews = GoogleNewsCN(start='05/20/2020', end='05/26/2020')
# # googlenews.setlang('en')
# # googlenews.search('taiwan')
# googlenews.clear()
# googlenews.getpage(2)
# result = googlenews.gettext()
# # result = googlenews.result()
# print(len(result))

# for result in googlenews.result():
#     print(result['title'], result['media'], result['date'])

# # page = 1
# # while 1:
# #     # googlenews.clear()
# #     googlenews.getpage(page)
# #     result = googlenews.gettext()
# #     if len(result) != 0:
# #         for result in googlenews.result():
# #             print(page, result['title'], result['media'], result['date'])
# #     page += 1

# https://www.google.com/search?q=abc+def&rlz=1C5CHFA_enTW890TW890&source=lnms&tbm=nws&sa=X&ved=2ahUKEwju_5DRmNTpAhUkE6YKHb7RCvoQ_AUoBHoECBIQBg&biw=1344&bih=706