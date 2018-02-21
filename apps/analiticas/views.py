from pymongo import MongoClient
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import simplejson as json

@csrf_exempt
def saveEvent(request):
    client = MongoClient('mongodb://admin:software2@ds241578.mlab.com:41578/guachita-analytics')
    db = client['guachita-analytics']

    eventox = request.POST.__getitem__('data')
    print(eventox)
    evento = json.loads(eventox)
    print('------------------------')
    print(evento)
    print('------------------------')
    db.eventos.save(evento)

    return HttpResponse("")

@csrf_exempt
def index2(request):
    pass
