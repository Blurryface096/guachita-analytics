from pymongo import MongoClient
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def saveEvent(request):
    client = MongoClient('mongodb://admin:software2@ds241578.mlab.com:41578/guachita-analytics')
    db = client['guachita-analytics']

    eventox = request.POST.__getitem__('data')
    print(eventox)
    print(type(eventox))
    evento = serializers.serialize('json', eventox)
    print('------------------------')
    print(evento)
    print(type(evento))
    db.eventos.save(evento)

    for e in db.eventos.find():
        print(e)

    return HttpResponse("")

@csrf_exempt
def index2(request):
    pass
