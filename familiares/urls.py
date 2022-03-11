from django.urls import path
from .views import familiares, crear_familiar

urlpatterns = [
    path('familiares/', familiares),
    path('nuevo-familiar/', crear_familiar)
]
