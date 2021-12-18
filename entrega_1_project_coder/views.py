from django.http import HttpResponse
from django.template import Template, Context, loader
from Entregable1.models import Partner, User
import os.path

def saludo(request):
    return HttpResponse("Hola Django")


def testTemplate(self):
    name = "Joni"
    lastname = "Gonzalez"

    dictionary = {
        "name": name,
        "lastname": lastname,
        "userId":""
    }
    template = loader.get_template("login.html")
    partner = User(userId=1999)
    dictionary["userId"] = partner.userId
    partner.save()
    document = template.render(dictionary)
    return HttpResponse(document)

