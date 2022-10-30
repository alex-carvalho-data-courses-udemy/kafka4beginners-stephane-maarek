import logging

from confluent_kafka import KafkaError, Message, SerializingProducer
from confluent_kafka.serialization import StringSerializer
from datetime import datetime


class KeyProducer:
    def __init__(self, target_topic: str) -> None:
        KeyProducer._init_log()

        self.producer = KeyProducer._create_producer()
        self.TARGET_TOPIC = target_topic

    @staticmethod
    def _init_log() -> None:
        logging.basicConfig(level=logging.INFO,
                            format='[%(asctime)s] %(levelname)s '
                                   '%(module)s.%(funcName)s(): %(message)s')

        logging.info('kafka producer with keys')

    @staticmethod
    def _create_producer() -> SerializingProducer:
        logging.info('creating kafka producer config')
        config = {
            'bootstrap.servers': 'localhost:19092,localhost:29092',
            'key.serializer': StringSerializer(),
            'value.serializer': StringSerializer()
        }

        logging.info('creating kafka producer')
        producer = SerializingProducer(config)

        return producer

    def produce(self) -> None:
        for i in range(10):
            key = f'id_{i}'
            msg = f'hello kafka topic from python with keys - {i} ' \
                  f'f - {datetime.now()}'
            logging.info(f'producing message key: {key} | value: {msg}'
                         f'to the topic {self.TARGET_TOPIC}')
            self.producer.produce(topic=self.TARGET_TOPIC,
                                  key=key,
                                  value=msg,
                                  on_delivery=KeyProducer._producer_callback)

        logging.info('flushing all messages to kafka')
        self.producer.flush()

    @staticmethod
    def _producer_callback(kafka_error: KafkaError,
                           message: Message) -> None:
        if not kafka_error:
            logging.info(f'message.error: {message.error()}')
            logging.info(f'message.headers: {message.headers()}')
            logging.info(f'message.key: {message.key()}')
            logging.info(f'message.latency: {message.latency()}')
            logging.info(f'message.offset: {message.offset()}')
            logging.info(f'message.partition: {message.partition()}')
            logging.info(f'message.timestamp: {message.timestamp()}')
            logging.info(f'message.topic: {message.topic()}')
            logging.info(f'message.value: {message.value()}')
        else:
            logging.error(f'kafka_error: {kafka_error}')
            logging.error(f'kafka_error.code: {kafka_error.code()}')
            logging.error(f'kafka_error.fatal: {kafka_error.fatal()}')
            logging.error(f'kafka_error.name: {kafka_error.name()}')
            logging.error(f'kafka_error.retriable: {kafka_error.retriable()}')
            logging.error(f'kafka_error.txn_requires_abort: '
                          f'{kafka_error.txn_requires_abort()}')
            logging.error(f'message.error: {message.error()}')
            logging.error(f'message.headers: {message.headers()}')
            logging.error(f'message.key: {message.key()}')
            logging.error(f'message.latency: {message.latency()}')
            logging.error(f'message.offset: {message.offset()}')
            logging.error(f'message.partition: {message.partition()}')
            logging.error(f'message.timestamp: {message.timestamp()}')
            logging.error(f'message.topic: {message.topic()}')
            logging.error(f'message.value: {message.value()}')


if __name__ == '__main__':
    KeyProducer('demo_python').produce()
