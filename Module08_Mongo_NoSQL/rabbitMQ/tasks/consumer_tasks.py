# Импортируем модуль pika для взаимодействия с RabbitMQ
import sys
import pika

# Импортируем модуль time для работы со временем
import time

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

# ! Создаем очередь с именем 'task_queue' и устанавливаем параметр durable=True, чтобы очередь сохранялась на диске при перезапуске сервера
channel.queue_declare(queue="task_queue", durable=True)
# Выводим сообщение о начале работы потребителя
print(" [*] Waiting for messages. To exit press CTRL+C")

# !Определяем функцию-обработчик сообщений из очереди
def callback(ch, method, properties, body):
    # ? Просто посмотреть что приходит
    # print(f"{ch}, {method}, {properties}, {body}")
    # Раскодируем полученное сообщение из JSON
    message = json.loads(body.decode())
    # Выводим сообщение в консоль
    print(f" [x] Received {message}")
    # Имитируем обработку задачи, засыпая на 1 секунду
    time.sleep(2)
    # Выводим сообщение о завершении обработки задачи
    print(f" [x] Done: {method.delivery_tag}")
    # Отправляем подтверждение о выполнении задачи в RabbitMQ
    ch.basic_ack(delivery_tag=method.delivery_tag)


# Устанавливаем максимальное количество сообщений, которые может обрабатывать потребитель одновременно, равным 1
channel.basic_qos(prefetch_count=1)
# Настраиваем потребителя на прослушивание очереди 'task_queue' с использованием функции-обработчика callback
channel.basic_consume(queue="task_queue", on_message_callback=callback)

# Если файл запускается напрямую, а не импортируется как модуль, начинаем прослушивание очереди
if __name__ == "__main__":
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)
