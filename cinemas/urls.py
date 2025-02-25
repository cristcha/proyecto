from django.urls import path
from . import views

urlpatterns = [
    
    # Cinemas
    path('', views.listarCinemas, name='listarCinemas'),
    path('agregar/', views.agregarCinema, name='agregarCinema'),
    path('editar/<int:pk>', views.editarCinema, name='editarCinema'),

    # Salas
    path('salas/', views.listarSalas, name='listarSalas'),
    path('agregar/sala/', views.agregarSala, name='agregarSala'),
    path('editar/sala/<int:pk>', views.editarSala, name='editarSala'),
]
