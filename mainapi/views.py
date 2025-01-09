from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from mainapi import models
from .models import User
import json
import code
# Create your views here.
interact = lambda : code.interact(local=locals())

def hello(request):
    d = {"status": "ok"}
    return JsonResponse(d)


@csrf_exempt
def send_message(request):
    if request.method != "POST":
        return JsonResponse({"status":"err","body":"Method have to be POST"})
    msg = {}
    try:
        msg = json.loads(request.body.decode())
    except json.JSONDecodeError:
        return JsonResponse({"status":"err","body":"Error leyendo JSON"})
    msg_type = msg["type"]
    msg_body = msg["text"]
    token = msg["token"]
    room = msg["room"]
    try:
        remitente = models.User.objects.get(token=token) 
    except models.User.DoesNotExist:
        return JsonResponse({"status":"err","body":"Token invalido"})
    try:
        room = models.Room.objects.get(nombre=room) 
    except models.Room.DoesNotExist:
        return JsonResponse({"status":"err","body":"Token invalido"})
    if msg_type & 1 == 1: # text
        models.Message(remitente=remitente, text=msg_body, room=room, message_type=msg_type ).save()
    if msg_type & 2 == 2: # image
        #models.Message(remitente=remitente, text=msg_body, room=room, message_type=msg_type ).save()
        pass
    if msg_type & 3 == 3: # audio
        #models.Message(remitente=remitente, text=msg_body, room=room, message_type=msg_type ).save()
        pass
    return JsonResponse({"status":"ok"})


def read_message(request):
    if request.method != "GET":
        return JsonResponse({"status":"err","body":"Method have to be GET"})
    msg = []
    filters = {}
    try:
        token = msg["token"]
        try:
            remitente = models.User.objects.get(token=token) 
        except models.User.DoesNotExist:
            return JsonResponse({"status":"err","body":"Token invalido"})
        room = msg["room"]
        try:
            room = models.Room.objects.get(nombre=room) 
        except models.Room.DoesNotExist:
            return JsonResponse({"status":"err","body":"Token invalido"})
        date = msg["date"]
        msg_id = msg["msg_id"]
        if msg_id != "":
            filters["id__gt"] = msg_id
        if date != "":
            filters["date__gt"] = date

    except:
        return JsonResponse({"status":"err","body":"Falta algun campo obligatorio"})
    return JsonResponse({"status":"ok"})


