import requests
import urllib
import logging
import time
import datetime as dt
from urllib.parse import quote, quote_plus
# from urllib.parse import quote
from bs4 import BeautifulSoup as Soup

logger = logging.getLogger(__name__)


class GoogleNewsSearch:

    def __init__(self, query="", tbm="nws",
                 start_date=None,
                 end_date=dt.datetime.strftime(dt.datetime.now(), '%m/%d/%Y'),
                 lang=None, period=None, result_per_page=20, pages=1):
        self.query = quote_plus(query)
        self.tbm = tbm
        self.start_date = start_date
        self.end_date = end_date
        self.period = period
        self.result_per_page = result_per_page
        self.pages = pages
        self.lang = lang
        self.user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
        self.headers = {'User-Agent': self.user_agent}
        self.results = []

    def getpage(self, page=1, delay=2):

        url_param = {
            "tbm": self.tbm,
            "lang_": self.lang,
            "lang_1": self.lang,
            "qdr": self.period,
            "num": self.result_per_page,
            "start": (self.pages * (page - 1))
        }
        if self.start_date is not None and \
           self.end_date is not None:
            url_param["tbs"] = quote_plus("sbd:1,cdr:1,cd_min:{},cd_max:{}".format(self.start_date, self.end_date))

        try:
            url_tmp = "https://www.google.com/search?q={}".format(self.query)
            for k, v in url_param.items():
                if v is not None:
                    url_tmp += "&{}={}".format(k, v)

            self.url = url_tmp
            logger.debug(self.url)
        except Exception as e:
            raise e

        try:
            self.req = urllib.request.Request(self.url, headers=self.headers)
            self.response = urllib.request.urlopen(self.req)
            self.page = self.response.read()
            self.content = Soup(self.page, "html.parser")
            result = self.content.find_all("div", id="search")[0].find_all("g-card")
            for item in result:
                try:
                    tmp_text = item.find("div", {"role" : "heading"}).text.replace("\n","")
                except Exception:
                    tmp_text = ''
                try:
                    tmp_link = item.find("a").get("href")
                except Exception:
                    tmp_link = ''
                try:
                    tmp_media = item.findAll("g-img")[1].parent.text
                except Exception:
                    tmp_media = ''
                try:
                    tmp_date = item.find("div", {"role" : "heading"}).next_sibling.findNext('div').findNext('div').text
                except Exception:
                    tmp_date = ''
                try:
                    tmp_desc = item.find("div", {"role" : "heading"}).next_sibling.findNext('div').text.replace("\n","")
                except Exception:
                    tmp_desc = ''
                try:
                    tmp_img = item.findAll("g-img")[0].find("img").get("src")
                except Exception:
                    tmp_img = ''
                # self.__texts.append(tmp_text)
                # self.__links.append(tmp_link)
                # self.__results.append({'title': tmp_text, 'media': tmp_media,'date': tmp_date,'desc': tmp_desc, 'link': tmp_link,'img': tmp_img})

                self.results.append({
                    'title': tmp_text,
                    'media': tmp_media,
                    'date': tmp_date,
                    'desc': tmp_desc,
                    'link': tmp_link,
                    'img': tmp_img})

                if "週前" in tmp_date:
                    dt_tmp_date = dt.datetime.strptime(tmp_date, "%d 週前")
                    weeks_ago = dt_tmp_date.day  # use "day" variable representing weeks
                    tmp_date = dt.datetime.now() - dt.timedelta(weeks=weeks_ago)
                elif "天前" in tmp_date:
                    dt_tmp_date = dt.datetime.strptime(tmp_date, "%d 天前")
                    days_ago = dt_tmp_date.day
                    tmp_date = dt.datetime.now() - dt.timedelta(days=days_ago)
                elif "小時前" in tmp_date:
                    dt_tmp_date = dt.datetime.strptime(tmp_date, "%H 小時前")
                    hours_ago = dt_tmp_date.hour
                    tmp_date = dt.datetime.now() - dt.timedelta(hours=hours_ago)
                    # print("{} hours ago".format(hours_ago))
                elif "分鐘前" in tmp_date:
                    dt_tmp_date = dt.datetime.strptime(tmp_date, "%M 分鐘前")
                    mins_ago = dt_tmp_date.minute
                    tmp_date = dt.datetime.now() - dt.timedelta(minutes=mins_ago)
                else:
                    tmp_date = dt.datetime.strptime(tmp_date, "%Y年%m月%d日")
                logger.debug(tmp_media, tmp_date)
            self.response.close()
        except Exception as e:
            logger.error(e)

        time.sleep(delay)

    def result(self):
        """Returns the __results."""
        return self.results

    def search():
        pass
