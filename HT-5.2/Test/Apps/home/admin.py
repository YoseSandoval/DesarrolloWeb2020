from django.contrib import admin
from .models import Estudiante, Administrador, Catedratico, Curso
# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Administrador)
admin.site.register(Catedratico)
admin.site.register(Curso)
