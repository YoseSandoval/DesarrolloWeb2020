from django.db import models

# Create your models here.
class Catedratico(models.Model):
    nombre_Catedratico = models.CharField(max_length=50)
    apellido_Catedratico = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=50)
    creacion = models.DateField(auto_now_add = True)
    actualización = models.DateField(auto_now_add = True)

    def __str__(self):
        return '%s %s' % (self.nombre_Catedratico,self.apellido_Catedratico)

class Curso(models.Model):
    catedratico = models.ManyToManyField(Catedratico)
    nombre_Curso = models.CharField(max_length=50)
    creacion = models.DateField(auto_now_add = True)
    actualización = models.DateField(auto_now_add = True)

    def __str__(self):
        return '%s' % (self.nombre_Curso)

class Estudiante(models.Model):
    curso = models.ManyToManyField(Curso)
    nombre_Estudiante = models.CharField(max_length=50)
    apellido_Estudiante = models.CharField(max_length=50)
    carnet = models.CharField(max_length=15)
    creacion = models.DateField(auto_now_add = True)
    actualización = models.DateField(auto_now_add = True)

    def __str__(self):
        return '%s %s' % (self.nombre_Estudiante,self.apellido_Estudiante)

class Administrador(models.Model):
    nombre_Administrador = models.CharField(max_length=50)
    apellido_Administrador = models.CharField(max_length=50)
    carnet = models.CharField(max_length=15)
    creacion = models.DateField(auto_now_add = True)
    actualización = models.DateField(auto_now_add = True)

    def __str__(self):
        return '%s %s' % (self.nombre_Administrador,self.apellido_Administrador)

