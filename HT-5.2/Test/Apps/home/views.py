from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'
class EstudiantesView(TemplateView):
    template_name='estudiantes.html'

class AdministradoresView(TemplateView):
    template_name='administradores.html'

class CreditosView(TemplateView):
    template_name='creditos.html'

