

from google.appengine.ext import ndb

from cancion import Cancion

class Comentario(ndb.Model):

    texto = ndb.StringProperty(required=True)
    hora = ndb.DateTimeProperty(auto_now_add=True)
    email = ndb.StringProperty(required=True)
    cancion = ndb.KeyProperty(kind=Cancion)

