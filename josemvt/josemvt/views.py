from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime

def familiares (request):
    
    datos = {"nombre": ["Juana", "Leticia", "Susana", "Noelia", "Enrique"]}
    
    plantilla = loader.get_template("familiares.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)