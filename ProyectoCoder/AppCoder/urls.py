from django.urls import path

#from AppCoder.views import curso, profesores     ----> si hago así, en el path no es necesario agregar views.
from AppCoder import views     #***hace algo similar al de arriba, solo que acá importo en general el views y no solo las clases curso y profe

urlpatterns = [
    path('profesores/', views.profesores),    #cuando lo generamos en la app, debemos cargar con el views.
    path('curso/', views.curso),
    
]
