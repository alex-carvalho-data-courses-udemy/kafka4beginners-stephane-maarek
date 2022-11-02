import logging

from confluent_kafka import DeserializingConsumer, KafkaException, KafkaError
from confluent_kafka.error import ConsumeError
from confluent_kafka.serialization import StringDeserializer

TARGET_TOPIC = 'demo_python'


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s] %(levelname)s '
                               '%(module)s %(funcName)s(): %(message)s')

    logging.info('kafka consumer with graceful shutdown')

    logging.info('create kafka consumer config...')
    config = {
        'bootstrap.servers': 'localhost:19092,localhost:29092,localhost:39092',
        'key.deserializer': StringDeserializer(),
        'value.deserializer': StringDeserializer(),
        'group.id': 'my-third-application',
        'auto.offset.reset': 'earliest',
        'enable.partition.eof': 'True',
    }

    logging.info('creating kafka consumer...')
    consumer = DeserializingConsumer(config)

    logging.info(f'subscribing topic {TARGET_TOPIC}')
    consumer.subscribe(topics=[TARGET_TOPIC])

    try:
        while True:
            try:
                # logging.info('kafka consumer polling...')
                msg = consumer.poll(timeout=1.0)

                if msg:
                    logging.info(f'key: {msg.key()}, value: {msg.value()}')
                    logging.info(f'partition: {msg.partition()}, '
                                 f'offset: {msg.offset()}')

            except KafkaException as ke:
                if ke.code == KafkaError._PARTITION_EOF:
                    logging.info('all messages read')
                else:
                    raise ke

    finally:
        consumer.close()
        logging.info('consumer closed')
