
import time
import webapp2
from webapp2_extras import jinja2

from model.cancion import Cancion
from webapp2_extras.users import users

class BuscarHandler(webapp2.RequestHandler):
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
        buscarTitulo = self.request.get("buscarTitulo","")

        usr = users.get_current_user()

        if usr:
            url_usr = users.create_logout_url("/")
        else:
            url_usr = users.create_login_url("/")


        if  not(buscarTitulo) :
            return self.redirect("/")
        else:
            cancionesEncontradas = []
            cancionesBuscadas = Cancion.query()

            for cancion in cancionesBuscadas:
                if buscarTitulo.lower() in cancion.titulo.lower() or buscarTitulo.lower() in cancion.artista.lower():
                    cancionesEncontradas.append(cancion)

            valores_plantilla = {
                "usr": usr,
                "url_usr": url_usr,
                "canciones": cancionesEncontradas,
                "buscarTitulo" : buscarTitulo
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("cancionesBuscar.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/canciones/buscar', BuscarHandler)
], debug=True)