import pika
import sys
import json


from faker import Faker
import json
import connect
from models import Message




credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_mock', exchange_type='direct')
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_bind(exchange='task_mock', queue='task_queue')


def main():
    for i in range(40):
        message = Message(name=Faker().name(), email=f"{Faker().name()}@{Faker().domain_name()}")
        message.save()

        channel.basic_publish(
            exchange='task_mock',
            routing_key='task_queue',
            body=json.dumps(str(message.id)).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(" [x] Sent %r" % message.id)
    connection.close()


if __name__ == '__main__':
    main()