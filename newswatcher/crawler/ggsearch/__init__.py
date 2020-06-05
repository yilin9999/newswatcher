import requests
import urllib
import logging
import time
from urllib.parse import quote, quote_plus
# from urllib.parse import quote
from bs4 import BeautifulSoup as Soup

logger = logging.getLogger(__name__)


class GoogleNewsSearch:

    def __init__(self, query="", tbm="nws", start_date=None, end_date=None, lang=None, period=None, result_per_page=20, pages=1):
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
            "cd_min": self.start_date,
            "cd_max": self.end_date,
            "lang_": self.lang,
            "lang_1": self.lang,
            "qdr": self.period,
            "num": self.result_per_page,
            "start": (self.pages * (page - 1))
        }
        try:
            url_tmp = "https://www.google.com/search?q={}".format(self.query)
            for k, v in url_param.items():
                if v is not None:
                    url_tmp += "&{}={}".format(k, v)
            self.url = url_tmp
            logger.info(self.url)
        except Exception as e:
            raise e

        # print(self.url)
        try:
            self.req = urllib.request.Request(self.url, headers=self.headers)
            self.response = urllib.request.urlopen(self.req)
            self.page = self.response.read()
            self.content = Soup(self.page, "html.parser")
            result = self.content.find_all("div", class_="g")
            for item in result:
                try:
                    tmp_text = item.find("h3").text
                except Exception:
                    tmp_text = ''
                try:
                    tmp_link = item.find("h3").find("a").get("href")
                except Exception:
                    tmp_link = ''
                try:
                    tmp_media = item.find("h3").findNext('div').find_all("span")[0].text
                except Exception:
                    tmp_media = ''
                try:
                    tmp_date = item.find("h3").findNext('div').find_all("span")[2].text
                except Exception:
                    tmp_date = ''
                try:
                    tmp_desc = item.find("div", class_="st").text
                except Exception:
                    tmp_desc = ''
                try:
                    tmp_img = item.find("img").get("src")
                except Exception:
                    tmp_img = ''
                # self.__texts.append(tmp_text)
                # self.__links.append(tmp_link)
                self.results.append({'title': tmp_text, 'media': tmp_media,'date': tmp_date,'desc': tmp_desc, 'link': tmp_link,'img': tmp_img})
            self.response.close()
        except Exception as e:
            print(e)

        time.sleep(delay)

    def result(self):
        """Returns the __results."""
        return self.results

    def search():
        pass
