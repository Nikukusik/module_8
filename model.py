from mongoengine import *


class Contact(Document):
    _id = ObjectIdField()
    name = StringField(max_length=50)
    email = StringField(max_length=50)
    age = IntField(max_value=100)
    status = BooleanField(default=False)
