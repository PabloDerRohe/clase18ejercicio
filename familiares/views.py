from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from .models import Familiar

# Create your views here.

def familiares(request):
    
    datos = {}
    
    return render(request, 'familiares.html', datos)

def nuevo_familiar(request):
    nuevo_familiar = Familiar(
        nombre='Celia',
        apellido='Arcucci',
        edad = 30,
    )
    return HttpResponse(f'Familiar agregado {nuevo_familiar.nombre} {nuevo_familiar.apellido}')

