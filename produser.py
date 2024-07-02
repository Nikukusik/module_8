from model import Contact
from faker import Faker
import pika
import json
from random import randint
import connection_to_db


def fake_contacts_to_db():
    contacts = Contact.objects()
    for contact in contacts:
        contact.delete()
    fake = Faker()
    for i in range(5):
        contact = Contact(name=fake.name(), age=randint(18,100), email=fake.email())
        contact.save()
def fake_contacts_to_queue(chanel):
    contacts = Contact.objects()
    for contact in contacts:
        chanel.basic_publish(exchange='', routing_key='mongodb', body=str(contact._id).encode())
        print(str(contact._id))


if __name__ == '__main__':
    fake_contacts_to_db()
    credentials = pika.PlainCredentials('user', 'password')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials))
    chanel = connection.channel()
    chanel.queue_declare(queue="mongodb")
    fake_contacts_to_queue(chanel)
    connection.close()
