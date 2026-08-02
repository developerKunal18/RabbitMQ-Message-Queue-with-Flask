import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="orders")

def callback(ch, method, properties, body):

    print("Received:", body.decode())

    ch.basic_ack(
        delivery_tag=method.delivery_tag
    )

channel.basic_consume(
    queue="orders",
    on_message_callback=callback
)

print("Waiting for messages...")

channel.start_consuming()
