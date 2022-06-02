from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre+" -Camada:"+str(self.camada)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profecion = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre+" "+str(self.profecion)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()

    