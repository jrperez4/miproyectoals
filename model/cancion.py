

from google.appengine.ext import ndb


class Cancion(ndb.Model):
    generos = ["Hip-Hop", "Reggaeton", "Rock", "Metal", "Pop"]
    titulo = ndb.StringProperty(required=True)
    artista = ndb.StringProperty(required=True)
    estilo = ndb.StringProperty(required=True, choices=generos)
    duracion = ndb.IntegerProperty(required=True)
