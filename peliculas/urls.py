from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.listarPeliculas, name='listarPeliculas'),
    path('agregar', views.agregarPelicula, name='agregarPelicula'),
    path('editar/<int:pk>', views.editarPelicula, name='editarPelicula'),
    path('eliminar/<int:pk>', views.eliminarPelicula, name='eliminarPelicula'),
]
