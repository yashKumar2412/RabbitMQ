import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

total_count = 0  # Global count variable

def callback(ch, method, properties, body):
    global total_count
    print(" [x] Received %r" % body)
    total_count += 1
    print(f"Total messages processed so far: {total_count}")

channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()