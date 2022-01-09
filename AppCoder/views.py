from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.

def crear_curso(self, nombre, camada):
    curso= Curso (nombre= nombre, camada= camada)
    curso.save()
    documentoDeTexto= f'Se creo el curso de {curso.nombre} de la camada {curso.camada}'
    return HttpResponse(documentoDeTexto)