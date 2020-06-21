from newswatcher.database import mgdb


class NewsMongoDoc:
    # title = mgdb.StringField(required=True)
    # media = mgdb.StringField()
    # date = mgdb.StringField()
    # desc = mgdb.StringField()
    # link = mgdb.ListField()
    # img = mgdb.ListField()

    # meta = {
    #         "collection": "news",
    #         "index": [{
    #             'fields': ['id'],
    #             'unique': True
    #         }]
    # }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    # db.news.createIndex({"link":1}, {unique: true})
    # db.news.createIndex({"title":1}, {unique: true})
    # db.news.createIndex({"media":1}, {unique: false})

    def __repr__(self):
        return '<NewsMongoDoc title:{0}>'.format(self.title)

    @classmethod
    def insert_one(self, input_dict):
        mgdb.db['news'].insert_one(input_dict)

    @classmethod
    def insert_many(self, input_array_dict, ordered):
        mgdb.db['news'].insert_many(input_array_dict, ordered=ordered)

    @classmethod
    def count_doc(self, doc_filter={}):
        return mgdb.db['news'].count_documents(doc_filter)

    # @classmethod
    # def insert_news(self):
    #     # pass
    #     # self.save()
