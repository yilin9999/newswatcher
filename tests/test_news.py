from newswatcher.crawler.views import search_news


class TestNews:

    def test_search_news(self, test_app):
        search_news()
