import pika
import json

class RabbitMQConsumer:
    def __init__(self, queue_name, callback):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    def start_consuming(self):
        print(f"[*] Waiting for messages in {self.queue_name}. To exit press CTRL+C")
        self.channel.start_consuming()

    def stop_consuming(self):
        self.channel.stop_consuming()
        self.connection.close()

