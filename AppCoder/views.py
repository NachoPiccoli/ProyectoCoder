import email
from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Profesor
# Create your views here.

def crear_profesor(request):

    profe= Profesor( nombre="ricardo", apellido= "rubio", email= "reik@hshs.com", profesion="abogado")

    profe.save()
    return HttpResponse(f"estoy creando al profe {profe.nombre} {profe.apellido} con mail {profe.email} y profesion {profe.profesion}")