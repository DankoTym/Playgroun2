from django.urls import path

#from AppCoder.views import curso, profesores     #----> si hago así, en el path no es necesario agregar views.
from AppCoder import views     #***hace algo similar al de arriba, solo que acá importo en general el views y no solo las clases curso y profe
# si hago lo de arriba, debo definir como views.curso o views.profesores en el path()


urlpatterns = [
    #path('profesores/', views.Profesores, name="profesores"),    #cuando lo generamos en la app, debemos cargar con el views.
    path('curso/', views.curso, name="curso"), 
    path('', views.Inicio, name="inicio"),
    path('cursos/', views.cursos, name="cursos"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('entregables/', views.entregables, name="entregables"),
    path('cursoFormulario/', views.cursoFormulario, name="cursoFormulario"),
    path('profesorFormulario/', views.profesorFormulario, name="profesorFormulario"),
    path('busquedaCamada/', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar, name="buscar"),
    #--------------CRUD clasico
    path('profesores/', views.leerProfesores, name="Profesores"), #modificamos la ruta profesores para no generar varias a lo mismo
    path('eliminarProfesor/<nombre>', views.eliminarProfesor, name="eliminarProfesor"),
    path('editarProfesor/<nombre>', views.editarProfesor, name="editarProfesor"),
    #--------------CRUD Desde Views----------------
    path('estudiante/lista/', views.EstudiantesList.as_view(), name="estudiante_list"),
    path('estudiante/<pk>', views.EstudiantesDitail.as_view(), name="estudiante_detalle"),        #el <pk> pasa de forma automatica el id por django
    path('estudiante/nuevo/', views.EstudianteCrear.as_view(), name="estudiante_crear"),
    path('estudiante/edit/<pk>', views.EstudianteEdicion.as_view(), name="estudiante_editar"),
    path('estudiante/delete/<pk>', views.EstudianteEliminacion.as_view(), name="estudiante_eliminar"),
    #---------------LOGIN--------------
    path('login', views.login_request, name="login"),
    path('registro', views.register_request, name="registro"), 
]