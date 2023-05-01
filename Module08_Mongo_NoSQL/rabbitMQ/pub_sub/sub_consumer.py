import pika
from datetime import datetime
import json

# Создаем объект pika.PlainCredentials для аутентификации в RabbitMQ с помощью учетных данных пользователя guest/guest
credentials = pika.PlainCredentials("guest", "guest")
# Создаем соединение с RabbitMQ, используя указанные параметры подключения и учетные данные
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
# Создаем канал для обмена сообщениями с RabbitMQ
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")
result = channel.queue_declare(queue="", exclusive=True)
name_of_queue = result.method.queue

channel.queue_bind(exchange="logs", queue=name_of_queue)
print(" [*] Waiting for messages. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue=name_of_queue, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
