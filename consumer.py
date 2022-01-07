import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

import django
django.setup()

from django.core.management import call_command

import json
import pika
from user_products.models import Product

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmqhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Main Received {data}")
    if properties.content_type == 'product_created':
        product = Product.objects.create(
            product_id=data['id'],
            title=data['title'],
            image=data['image']
        )
        product.save()
        print('Product created')
    elif properties.content_type == 'product_updated':
        product = Product.objects.get(pk=data['id'])
        product.title = data['title']
        product.image = data['image']
        product.save()
        print('Product updated')
    elif properties.content_type == 'product_deleted':
        product = Product.objects.get(pk=data['pk'])
        product.delete()
        print('Product deleted')


channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
channel.close()
