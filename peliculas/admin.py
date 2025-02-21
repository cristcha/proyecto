from django.contrib import admin
from .models import Pelicula, Genero, Clasificacion

admin.site.register([Pelicula, Genero, Clasificacion])
