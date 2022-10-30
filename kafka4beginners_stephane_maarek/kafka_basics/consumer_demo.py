import logging

from confluent_kafka import DeserializingConsumer, KafkaException, KafkaError
from confluent_kafka.serialization import StringDeserializer


TARGET_TOPIC = 'demo_python'


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s] %(levelname)s '
                               '%(module)s.%(funcName)s(): %(message)s')

    logging.info('kafka consumer')

    logging.info('creating kafka consumer config...')
    config = {
        'bootstrap.servers': 'localhost:19092,localhost:29092,localhost:39092',
        'key.deserializer': StringDeserializer(),
        'value.deserializer': StringDeserializer(),
        'group.id': 'my-second-application',
        'auto.offset.reset': 'earliest',
    }

    logging.info('creating kafka consumer...')
    consumer = DeserializingConsumer(config)

    logging.info(f'subscribing consumer to topic {TARGET_TOPIC}')
    consumer.subscribe(topics=[TARGET_TOPIC])

    while True:
        msg = consumer.poll(timeout=1.0)

        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                logging.info(f'Topic {msg.topic()}, '
                             f'partition {msg.partition()}'
                             f' reached the end at the offset {msg.offset()}')
            else:
                raise KafkaException(msg.error())
        else:
            logging.info(f'Key: {msg.key()}, value: {msg.value()}')
            logging.info(f'Partition: {msg.partition()}, '
                         f'offset: {msg.offset()}')
