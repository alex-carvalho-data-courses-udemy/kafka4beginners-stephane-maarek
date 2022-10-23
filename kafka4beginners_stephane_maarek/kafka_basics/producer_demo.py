import logging

from confluent_kafka.serialization import StringSerializer
from confluent_kafka import SerializingProducer
from datetime import datetime


class ProducerDemo:
    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s-%(filename)s-%(funcName)s()'
                                   '-%(levelname)s-%(message)s')
        logging.info('Initializing ProducerDemo')

        self._producer = ProducerDemo._create_producer()

    @staticmethod
    def _create_producer() -> SerializingProducer:
        logging.info('creating producer')
        config = {
            'bootstrap.servers': 'localhost:19092',
            'key.serializer': StringSerializer(),
            'value.serializer': StringSerializer()
        }

        return SerializingProducer(config)

    def send_data(self, topic: str, value: str) -> None:
        value = f'{value} - {datetime.now()}'

        logging.info(f'Producing to topic {topic} the message {value}')

        self._producer.produce(topic=topic, value=value)

    def close(self) -> None:
        logging.info('flushing messages')
        self._producer.flush()


if __name__ == '__main__':
    TOPIC_NAME = 'demo_java'

    producer = ProducerDemo()

    producer.send_data(topic=TOPIC_NAME, value='hello world')

    # Flush and close the Producer
    producer.close()
