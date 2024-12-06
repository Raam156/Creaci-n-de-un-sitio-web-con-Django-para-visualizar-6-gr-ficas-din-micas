from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ajusta la vista según tu implementación
]
