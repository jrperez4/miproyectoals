#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2

from webapp2_extras import jinja2

from model.comentario import Comentario
from model.cancion import Cancion
from webapp2_extras.users import users

import time
from datetime import datetime




class NuevoComentarioHandler(webapp2.RequestHandler):
    def post(self):

        usr = users.get_current_user()
        cancion = Cancion.recupera(self.request)


        if usr:
            comentario = self.request.get("edComentario", "")

            if not (comentario):
                return self.redirect("/")
            else:

                comentarioNuevo = Comentario(texto=comentario, hora=datetime.now(), email=usr.email(), cancion=cancion.key)
                comentarioNuevo.put()
                time.sleep(1)
                return self.redirect("/canciones/comentarios?id=" + cancion.key.urlsafe())





        else :
            return self.redirect("/")







app = webapp2.WSGIApplication([
    ('/comentarios/nuevo', NuevoComentarioHandler)
], debug=True)
