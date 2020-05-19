# Usuario registrado en la aplicacion

from google.appengine.ext import ndb

class User(ndb.Model):

    nombre = ndb.StringProperty(required=True)
    contraseña = ndb.StringProperty(required=True)
    
