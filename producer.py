import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

message_count = 1000000

for i in range(0, message_count):
    message = 'message ' + str(i)
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(" [x] Sent message")

connection.close()