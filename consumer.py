import bson
import pika
import connection_to_db
from model import Contact
import json




credentials = pika.PlainCredentials("user", "password")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials))
chanel = connection.channel()
chanel.queue_declare(queue="mongodb")

def send_email(message):
    print("email sended")
def callback(ch, method, priorities, body):
    message = body.decode()
    contact = Contact.objects(_id=message)
    contact.update(status=True)
    send_email(contact)

chanel.basic_consume(queue='mongodb', on_message_callback=callback)


if __name__ == "__main__":
    chanel.start_consuming()

