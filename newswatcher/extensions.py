import json
import datetime as dt
from kafka import KafkaProducer, KafkaConsumer


kafka_producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda x: json.dumps(x).encode('utf-8'))

kafka_consumer = KafkaConsumer(
            bootstrap_servers='localhost:9092',
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            # auto_offset_reset='earliest',
            consumer_timeout_ms=1000)

# kafka_consumer.subscribe(AppConfig.KAFKA_TOPIC_MONGODB)


class KafkaQueueItem():
    def __init__(self, body, time_elapsed):
        self.time_elapsed = time_elapsed
        if body is dict:
            self.data = [body]
        else:
            self.data = body
        self.data_cnt = len(self.data)

    @property
    def items(self):
        return {
            "time_elapsed": self.time_elapsed,
            "data_cnt": self.data_cnt,
            "data": self.data
        }
