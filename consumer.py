import pika

params = pika.URLParameters(
    "amqps://ohwpsrxf:gl13qpU8lccWdIL0BQJEMN7KoM-8HIjr@eagle.rmq.cloudamqp.com/ohwpsrxf"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="main")


def callback(ch, method, properties, body):
    print("Recieved in main")
    print(body)


channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

print("Started consuming")
channel.start_consuming()

channel.close()
