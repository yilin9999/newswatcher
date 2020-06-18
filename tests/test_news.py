import json
from urllib.parse import quote_plus
# from newswatcher.crawler.views import crawler_search_news


class TestNews:

    def test_crawler_search_news(self, client):
        data = {
            "queries": [
                "報導者The Reporter",
                #quote_plus("報導者The Reporter"),
                "ETtoday"
            ],
            "start_date": "2020-06-17T00:00:00Z",
            "end_date": "2020-06-17T23:59:59Z"
        }
        resp = client.post("/crawler", data=json.dumps(data).encode('utf-8'))
        assert resp.status_code == 200
        # crawler_search_news()
