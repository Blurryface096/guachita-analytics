from pymongo import MongoClient
from django.http import HttpResponse
from django.core import serializers

def saveEvent(request):
    client = MongoClient('mongodb://admin:software2@ds241578.mlab.com:41578/guachita-analytics')
    db = client['guachita-analytics']
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

def index2(request):
    lista = ['1', '2']
    srslst = serializers.serialize('json', lista)
    return HttpResponse(srslst, content_type='application/json')
