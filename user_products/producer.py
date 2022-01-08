import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmqhost'))
channel = connection.channel()

channel.queue_declare(queue='main')


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
    print(f"Send {body}")
