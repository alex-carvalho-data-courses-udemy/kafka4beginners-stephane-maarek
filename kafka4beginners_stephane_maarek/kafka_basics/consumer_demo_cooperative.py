import logging

from confluent_kafka import DeserializingConsumer
from confluent_kafka.serialization import StringDeserializer

TARGET_TOPIC = 'demo_python'


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] %(levelname)s '
                               '%(name)s-%(funcName)s: %(message)s')

    logger = logging.getLogger(__name__)

    logger.info('kafka consumer cooperative rebalancing')

    logger.debug('creating kafka config..')
    config = {
        'bootstrap.servers': 'localhost:19092,localhost:29092,localhost:39092',
        'key.deserializer': StringDeserializer(),
        'value.deserializer': StringDeserializer(),
        'group.id': 'my-third-application',
        'auto.offset.reset': 'earliest',
        'logger': logger,
        'partition.assignment.strategy': 'cooperative-sticky'
    }

    logger.debug('creating kafka consumer..')
    consumer = DeserializingConsumer(config)

    logger.info(f'subscribing kafka topic {TARGET_TOPIC}')
    consumer.subscribe(topics=[TARGET_TOPIC])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)

            if msg:
                logger.info(f'msg - key: {msg.key()}, value: {msg.value()}')

    finally:
        consumer.close()
        logger.error('kafka consumer is closed')
