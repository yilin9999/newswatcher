import json
from urllib.parse import quote_plus
# from newswatcher.crawler.views import crawler_search_news


class TestCrawler:

    def test_crawler_search_news(self, client):
        data = {
            "queries": [
                "報導者The Reporter",
                # quote_plus("報導者The Reporter"),
                "ETtoday"
            ],
            "start_date": "6/13/2020",
            "end_date": "6/20/2020"
        }
        resp = client.post("/crawler", data=json.dumps(data).encode('utf-8'))
        assert resp.status_code == 200
        # print(resp)
        # crawler_search_news()
