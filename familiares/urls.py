from django.urls import path
from .views import nuevo_familiar

urlpatterns = [
    path('familiares.html', familiares)
    path('nuevo-familiar', nuevo_familiar)
]
