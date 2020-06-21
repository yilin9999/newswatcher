def template(data, code=500):
    return {'message': {'errors': {'body': data}}, 'status_code': code}


KAFKA_PRODUCER_FAILED = template(['kafka producer failed'], code=404)


class RunTimeError(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    @classmethod
    def kafka_producer_fail(cls):
        return cls(**KAFKA_PRODUCER_FAILED)
