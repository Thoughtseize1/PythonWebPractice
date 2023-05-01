# Импортируем модуль pika для взаимодействия с RabbitMQ
import pika

# Импортируем модуль json для работы с JSON
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

if __name__ == "__main__":
    channel.basic_publish(
        exchange="logs",
        routing_key="",
        body="Hello World! WEB9! + NIKITOS222 :)".encode(),
    )
    connection.close()
