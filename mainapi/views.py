from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
    if msg_type & 1 == 1: # text
        pass

    return JsonResponse({"status":"ok"})




