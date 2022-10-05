from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from Personas.models import Persona

def crear_persona(request):
    persona1 = Persona(nombre='Lucia', apellido='Gonzalez',fecha_de_creacion= datetime.now(), edad=32)
    persona1.save()

    persona2 = Persona(nombre='Gustavo', apellido='Cerati',fecha_de_creacion= datetime.now(), edad=58)
    persona2.save()

    persona3 = Persona(nombre='Ricardo', apellido='Mollo',fecha_de_creacion= datetime.now(), edad=60)
    persona3.save()

    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({'personas' : persona1})
    template_renderizado = template.render({'personas' : persona2})
    template_renderizado = template.render({'personas' : persona3}) 
    return HttpResponse(template_renderizado)

def ver_personas(request):
    personas = Persona.objects.all()
    
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas': personas}) 
   
    return HttpResponse(template_renderizado)