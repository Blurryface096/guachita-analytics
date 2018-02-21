from mongoengine import Document, fields

class Event(Document):
    tipo = fields.StringField(required=True)
    URL_Actual = fields.StringField(required=True, null=True)
    URL_Destino = fields.StringField(required=True, null=True)
    Browser = fields.StringField(required=True, null=True)
    Plataforma = fields.StringField(required=True, null=True)
    Language = fields.StringField(required=True, null=True)
