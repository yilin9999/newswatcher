from marshmallow import Schema, fields


class GsearchConfigSchema(Schema):
    queries = fields.List(fields.String(), required=True)
    # start_date = fields.DateTime(required=True)
    start_date = fields.Date("%m/%d/%Y", required=True)
    end_date = fields.Date("%m/%d/%Y", required=True)
    # start_date = fields.DateTime("%d-%m-%Y", required=True)
    # end_date = fields.DateTime("%d-%m-%Y", required=True)


class GsearchRespSchema(Schema):
    job_uid = fields.String(required=True)
    created_at = fields.DateTime(required=True)


class GsearchResultSchema(Schema):
    status = fields.String(required=True)
    time_elapsed = fields.String(required=True)
