# coding: utf-8
import time
import webapp2
from webapp2_extras import jinja2

from model.cancion import Cancion
from webapp2_extras.users import users

class NuevaCancionHandler(webapp2.RequestHandler):
    def get(self):

        usr = users.get_current_user()

        if usr:
            url_usr = users.create_logout_url("/")
        else:
            url_usr = users.create_login_url("/")

        valores_plantilla = {
            "usr": usr,
            "url_usr": url_usr
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nueva_cancion.html", **valores_plantilla))


    def post(self):
        titulo = self.request.get("edTitulo","")
        artista = self.request.get("edArtista","")
        estilo = self.request.get("edEstilo","")

        str_duracion = self.request.get("edDuracion","")

        try:
            duracion = int(str_duracion)
        except ValueError:
            duracion = -1

        if duracion < 0 or not(titulo) or not(artista) or not(estilo):
            return self.redirect("/")
        else:
            cancion = Cancion(titulo=titulo, artista=artista, estilo=estilo, duracion=duracion)
            cancion.put()
            time.sleep(1)
            return self.redirect("/")







app = webapp2.WSGIApplication([
    ('/canciones/nueva', NuevaCancionHandler)
], debug=True)