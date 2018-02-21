from pymongo import MongoClient
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def saveEvent(request):
    client = MongoClient('mongodb://admin:software2@ds241578.mlab.com:41578/guachita-analytics')
    db = client['guachita-analytics']

    print(request.method)
    print(request.POST)
    evento = {
        'tipo' : 'click',
        'URL_Actual' : 'www.guachita.com',
        'URL_Destino' : 'www.guachita.com/home',
        'Browser' : 'Mozilla',
        'Plataforma' : 'Win32',
        'Language' : 'en-US',
    }

    db.eventos.save(evento)
    return HttpResponse("")

@csrf_exempt
def index2(request):
    pass
