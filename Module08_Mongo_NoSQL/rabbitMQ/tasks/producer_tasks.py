# Импортируем модуль pika для взаимодействия с RabbitMQ
import pika

# Импортируем класс datetime из стандартной библиотеки Python для работы с датой и временем
from datetime import datetime

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

# Создаем обменник типа direct с именем 'task_mock'
channel.exchange_declare(exchange="task_mock", exchange_type="direct")
# Создаем очередь с именем 'task_queue' и устанавливаем параметр durable=True, чтобы очередь сохранялась на диске при перезапуске сервера
channel.queue_declare(queue="task_queue", durable=True)
# Связываем созданный обменник с очередью 'task_queue'
channel.queue_bind(exchange="task_mock", queue="task_queue")

# Определяем функцию main
def main():
    # Отправляем 24 сообщения в очередь
    for i in range(24):
        # Создаем словарь-сообщение с уникальным идентификатором, текстом сообщения и текущим временем
        message = {
            "id": i + 1,
            "payload": f"Task #{i + 1}",
            "date": datetime.now().isoformat(),
        }
        # Отправляем сообщение в очередь 'task_queue' с помощью метода basic_publish канала
        # Сообщение кодируется в JSON и устанавливается свойство delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE для сохранения сообщения на диске
        channel.basic_publish(
            exchange="task_mock",
            routing_key="task_queue",
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
        # Выводим отправленное сообщение в консоль
        print(" [x] Sent %r" % message)
    # Закрываем соединение с RabbitMQ
    connection.close()


# Если файл запускается напрямую, а не импортируется как модуль, вызываем функцию main
if __name__ == "__main__":
    main()
