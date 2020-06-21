from marshmallow import Schema, fields


class NewsSchema(Schema):
    time_elapsed = fields.Float(required=True)
    data_cnt = fields.Integer(required=True)
    data = fields.List(fields.Dict, required=True)
    # start_date = fields.DateTime("%d-%m-%Y", required=True)
    # end_date = fields.DateTime("%d-%m-%Y", required=True)
