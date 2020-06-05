from newswatcher.database import mgdb


class NewsDoc:
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

    def __repr__(self):
        return '<NewsDoc title:{0}>'.format(self.title)

    @classmethod
    def insert_one(self, input_dict):
        mgdb.db['news3'].insert_one(input_dict)

    @classmethod
    def insert_many(self, input_array_dict):
        mgdb.db['news'].insert_many(input_array_dict)

    # @classmethod
    # def insert_news(self):
    #     # pass
    #     # self.save()
