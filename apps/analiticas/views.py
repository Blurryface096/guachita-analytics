from pymongo import MongoClient
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
import json as json2
from bson import ObjectId
from bson.son import SON



@csrf_exempt
def saveEvent(request):
    client = MongoClient('mongodb://admin:software2@ds241578.mlab.com:41578/guachita-analytics')
    db = client['guachita-analytics']

    eventox = request.POST.__getitem__('data')
    #print(eventox)
    evento = json.loads(eventox)
    print('------------------------')
    print(evento)
    print('------------------------')
    db.eventos.save(evento)

    return HttpResponse("")

@csrf_exempt
def getReport(request):
    client = MongoClient('mongodb://admin:software2@ds241578.mlab.com:41578/guachita-analytics')
    db = client['guachita-analytics']

    eventos = db.eventos.find()
    lst_eventos = []
    for e in eventos:
        lst_eventos.append(e)
    temp = {
        'collection' : lst_eventos
    }
    json_report = JSONEncoder().encode(temp)

    return HttpResponse(json_report, content_type='application/json')

@csrf_exempt
def getVistasDiarias(request):
    client = MongoClient('mongodb://admin:software2@ds241578.mlab.com:41578/guachita-analytics')
    db = client['guachita-analytics']
    pipeline = [
        {"$group" : {"_id":"$Date", "total": {"$sum":1}},
        {"$sort": SON([("total", -1), ("_id", -1)])}
    }]
    eventos = db.eventos.aggregate(pipeline)
    #eventos = db.eventos.find()
    lst_eventos = []
    for e in eventos:
        lst_eventos.append(e)
    temp = {
        'visitas' : lst_eventos
    }
    json_report = JSONEncoder().encode(temp)

    return HttpResponse(json_report, content_type='application/json')


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json2.JSONEncoder.default(self, o)
