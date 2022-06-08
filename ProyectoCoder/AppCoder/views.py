from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Profesor
from django.template import loader
from AppCoder.forms import CursoFormulario, ProfesorFormulario

# Create your views here.
def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada=16740)
    curso.save()
    documento = f"curso: {curso.nombre} - camada: {curso.camada}"
    return HttpResponse(documento)

def Profesores(request):
    
    return render(request, 'AppCoder/profesores.html')

def cursos(request):
    
    return render(request, 'AppCoder/cursos.html')

def estudiantes(request):
    
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    
    return render(request, 'AppCoder/entregables.html')

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        nombre = informacion['curso']
        camada = informacion['camada']
        curso = Curso(nombre=nombre, camada=camada)
        curso.save()
        return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()
    return render(request, 'AppCoder/cursoFormulario.html', {'miFormulario':miFormulario})




def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        email = informacion['email']
        profecion = informacion['profecion']

        profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profecion=profecion)
        profesor.save()
        return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ProfesorFormulario()

    return render(request, 'AppCoder/profesorFormulario.html', {'miFormulario':miFormulario})



def busquedaCamada(request):        #Esta buncion solo recibe el numero de camada que quiero buscar

    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):               #Esta es la funcion que busca la camada

    #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
    if request.GET['camada']:
        camada =request.GET['camada']               #Hace que camada sea igual a lo que me mandan desde la vista.
        cursos = Curso.objects.filter(camada=camada)    #Realisa una comparacion entre lo que busco y lo que hay cargado.
        return render(request, "AppCoder/resultadosBusqueda.html", {'cursos':cursos, 'camada':camada})
    else:
        respuesta = "No se ingreso ninguna comisión" 
        return HttpResponse(respuesta)


def Inicio(self):
    plantilla = loader.get_template('AppCoder/inicio.html')   #es importante que la pagina de inicio, tenga un loader.
    documento = plantilla.render()
    return HttpResponse(documento)


#-----------------Clase 22: ---------------

def leerProfesores(request):
    profesores = Profesor.objects.all() #crea una variable de tipo Profesor que trar todos los objetos de este (.all)
    contexto = {'profesores':profesores}    #crea un diccionario que pasa el "contexto" de los elementos de Profesores
    return render(request, 'AppCoder/profesores.html', contexto)    #acá pasamos el contexto al .html


#eliminar elementos

def eliminarProfesor(request, nombre):
    profesor = Profesor.objects.get(nombre=nombre)      #busca el elemento nombre que le paso desde la web
    profesor.delete()                                   #si lo encuentra lo elimina

    profesores = Profesor.objects.all()                 #recarga lo elementos profesores existentes
    contexto = {'profesores':profesores}
    return render(request, 'AppCoder/profesores.html', contexto)    #vuelve al menú con los nuevos elementos

# ACTUALIZAR ELEMENTOS:

def editarProfesor(request, nombre):
    profesor = Profesor.objects.get(nombre=nombre)      #traemos el elemento quye queremos modificar
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion['nombre']         #a diferencia del formulario, acá anteponemos el profesor. porque lo que está 
            profesor.apellido = informacion['apellido']     #haciendo es extraer ese elemento, no cargando en una nueva variable
            profesor.email = informacion['email']
            profesor.profecion = informacion['profecion']
            profesor.save()

            profesores = Profesor.objects.all()                 
            contexto = {'profesores':profesores}
            return render(request, 'AppCoder/profesores.html', contexto)
    else:
        miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'profecion':profesor.profecion})
        contexto = {'miFormulario':miFormulario, 'nombre':nombre}
        return render(request, 'AppCoder/editarProfesor.html', contexto)