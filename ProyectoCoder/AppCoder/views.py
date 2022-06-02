from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.template import loader

# Create your views here.
def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada=16740)
    curso.save()
    documento = f"curso: {curso.nombre} - camada: {curso.camada}"
    return HttpResponse(documento)

def profesores(self):
    documento = f"Pagina de profesores"
    return HttpResponse(documento)

def cursos(self):
    documento = f"Pagina de Cursos"
    return HttpResponse(documento)

def estudiantes(self):
    documento = f"Pagina de estudiantes"
    return HttpResponse(documento)

def entregables(self):
    documento = f"Pagina de entregables"
    return HttpResponse(documento)

def Inicio(self):
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)
 