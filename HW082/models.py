
from mongoengine import  Document
from mongoengine.fields import BooleanField, StringField


class Message(Document):
    name = StringField()
    email = StringField()
    is_send = BooleanField(default=False)

