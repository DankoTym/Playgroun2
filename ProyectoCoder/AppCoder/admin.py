from django.contrib import admin
from .models import Curso, Estudiante, Entregable, Profesor 

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)

# Register your models here.
