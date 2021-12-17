from django.http import HttpResponse
from django.template import Template, Context, loader
import os.path

def saludo(request):
    return HttpResponse("Hola Django")


def testTemplate(self):
    name = "Joni"
    lastname = "Gonzalez"

    dictionary = {
        "name": name,
        "lastname": lastname
    }

    template = loader.get_template("login.html")
    document = template.render(dictionary)

    return HttpResponse(document)

