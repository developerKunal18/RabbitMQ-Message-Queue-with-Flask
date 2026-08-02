import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="orders")

channel.basic_publish(
    exchange="",
    routing_key="orders",
    body="New Order #1001"
)

print("Message Sent")

connection.close()
