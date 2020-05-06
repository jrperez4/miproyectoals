

from google.appengine.ext import ndb

from user import User
from cancion import Cancion

class Comentario(ndb.Model):

    hora = ndb.DateTimeProperty(auto_now_add=True)
    usuario = ndb.KeyProperty(kind=User)
    cancion = ndb.KeyProperty(kind=Cancion)
