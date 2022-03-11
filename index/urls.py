from django.urls import path
from .views import index, plantilla

urlpatterns = [
    # El path debe tener la direccion, nombre de la vistas y nombre
    # para identificar la vista
    path('', index, name='index'),
    path('plantilla/', plantilla, name='plantilla')
]
