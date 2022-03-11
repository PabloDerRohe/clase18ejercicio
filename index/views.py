from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenidos a mi pagina de django</h1>')

# def plantilla(request):
    
#     template = loader.get_template('plantilla.html')
    
#     datos = {
#         'lista':['primero', 'segundo', 'tercero'],
#         'nombre': 'Juancho'
#     }
    
#     plantilla_generada = template.render(datos)
    
#     return HttpResponse(plantilla_generada)

def plantilla(request):
        
    datos = {
        'lista':['primero', 'segundo', 'tercero'],
        'nombre': 'Juancho'
    }
        
    return render(request, 'index/plantilla.html', datos)