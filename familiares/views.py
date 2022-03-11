from django.shortcuts import render
from django.http import HttpResponse
from familiares.models import Familiar

# Create your views here.


def familiares(request):
    
    datos = {}
    
    return render(request, 'familiares.html', datos)


def crear_familiar(request):
    
    crear_familiar = Familiar(
        nombre='Rambo',
        apellido='Arcucci-Marelli',
        edad = 0,
        hobby = 'Morder a Fili'
    )
    crear_familiar.save()
    
    return HttpResponse(f'Familiar agregado {crear_familiar.nombre} {crear_familiar.apellido}')

