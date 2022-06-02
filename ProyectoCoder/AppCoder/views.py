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

def profesores(request):
    
    return render(request, 'AppCoder/profesores.html')

def cursos(request):
    
    return render(request, 'AppCoder/cursos.html')

def estudiantes(request):
    
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    
    return render(request, 'AppCoder/entregables.html')

def Inicio(self):
    plantilla = loader.get_template('AppCoder/inicio.html')   #es importante que la pagina de inicio, tenga un loader.
    documento = plantilla.render()
    return HttpResponse(documento)
 