import json
import logging

logger = logging.getLogger(__name__)


class TestStorage:

    def test_store_mongo(self, client):
        data = {
            "time_elapsed": 3.05,
            "data_cnt": 50,
            "data": [
                {
                    "title": "總舖師與水腳最漫長的寒冬",
                    "media": "報導者The Reporter",
                    "date": "2017-07-21T17:32:28Z",
                    "desc": "《報導者》採訪南、北部近10名總舖師",
                    "link": "https://www.twreporter.org/",
                    "img": "https://encrypted-tbn0.gstatic.com/images?xxx"
                }
            ]
        }
        resp = client.post("/storage/mongo", data=json.dumps(data).encode('utf-8'))
        assert resp.status_code == 201
        logger.info(resp.status)
