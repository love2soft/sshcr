from django.db import models
import json

# Create your models here.

string = lambda x: models.CharField(max_length=x)
number = lambda : models.IntegerField()
remote = lambda x: models.ForeignKey(x, on_delete=models.CASCADE)
photo = lambda : models.ImageField(upload_to="./images")
timestamp = lambda : models.DateTimeField(auto_now=True)
m2m = lambda x: models.ManyToManyField(x)

class User(models.Model):
    username = string(30)
    nombre = string(36)
    foto = photo()
    descripcion = string(255)
    token = string(64)

    def __str__(self):
        return str(self.nombre)


class Room(models.Model):
    nombre = string(30)
    foto = photo()
    users = m2m(User)

    def __str__(self):
        return str(self.nombre)


class Message(models.Model):
    remitente = remote(User)
    message_type = number()
    room = remote(Room)
    text = string(500)
    date = timestamp()

    def jsonify(self):
        d = {"remitente": self.remitente.nombre,
             "room": self.room.nombre,
             "test": self.text,
             "date": str(self.date),
             "message_type": self.message_type}
        return d

    def __str__(self):
        return str(self.remitente)+": " + str(self.text)

