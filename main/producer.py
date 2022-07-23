import pika
import json
import os


params = pika.URLParameters(os.getenv('RABBITMQ_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
