from django.shortcuts import render, redirect, get_object_or_404
from .models import Pelicula, Genero, Clasificacion
from datetime import datetime

def listarPeliculas(request):
    
    peliculas = Pelicula.objects.all()
    
    contexto = {
        'peliculas': peliculas,
    }    
    return render(request, 'peliculas/listar.html', context=contexto)

def agregarPelicula(request):
    
    if request.method == 'POST':
        poster = request.FILES['poster']
        nombre = request.POST['nombre']
        sinopsis = request.POST['sinopsis']
        reparto = request.POST['reparto']
        director = request.POST['director']
        
        # Formatear fecha
        fecha_estreno = request.POST['fecha_estreno']
        fecha_estreno = datetime.strptime(fecha_estreno, "%Y-%m-%d")

        trailer = request.POST['trailer']
        duracion = request.POST['duracion']
        
        # Obtener instancia genero
        genero = request.POST['genero']
        genero = Genero.objects.get(id_genero=genero)
        
        # Obtener instancia clasificacion
        clasificacion = request.POST['clasificacion']
        clasificacion = Clasificacion.objects.get(id_clasificacion=clasificacion)
        
        Pelicula.objects.create(poster=poster, nombre=nombre, sinopsis=sinopsis, reparto=reparto, director=director,fecha_estreno=fecha_estreno, trailer=trailer, duracion=duracion, id_genero=genero, id_clasificacion=clasificacion)
        
        return redirect('listarPeliculas')
        
    else:
   
        generos = Genero.objects.all()
        clasificaciones = Clasificacion.objects.all()
        
        contexto = {
            'generos': generos,
            'clasificaciones': clasificaciones,
        }
        
        return render(request, 'peliculas/agregar.html', context=contexto)


def editarPelicula(request, pk):
    
    # Obtener datos actuales de la película
    pelicula = get_object_or_404(Pelicula, pk=pk)
    
    if request.method == 'POST':
        poster = request.FILES['poster']
        nombre = request.POST['nombre']
        sinopsis = request.POST['sinopsis']
        reparto = request.POST['reparto']
        director = request.POST['director']
        fecha_estreno = request.POST['fecha_estreno']
        trailer = request.POST['trailer']
        duracion = request.POST['duracion']
        genero = request.POST['genero']
        clasificacion = request.POST['clasificacion']
        
        # Validar que campos tuvieron cambios y asignar nuevo valor
        if pelicula.poster != poster:
            pelicula.poster = poster
            
        if pelicula.nombre != nombre:
            pelicula.nombre = nombre
            
        if pelicula.sinopsis != sinopsis:
            pelicula.sinopsis = sinopsis
            
        if pelicula.reparto != reparto:
            pelicula.reparto = reparto
            
        if pelicula.director != director:
            pelicula.director = director
            
        if pelicula.fecha_estreno != fecha_estreno:
            pelicula.fecha_estreno = fecha_estreno
            
        if pelicula.trailer != trailer:
            pelicula.trailer = trailer
            
        if pelicula.duracion != duracion:
            pelicula.duracion = duracion

        if pelicula.id_genero != genero:
            pelicula.id_genero = Genero.objects.get(pk=genero)

        if pelicula.id_clasificacion != clasificacion:
            pelicula.id_clasificacion = Clasificacion.objects.get(pk=clasificacion)
        
        # Guardar cambios
        pelicula.save()
        return redirect('listarPeliculas')
        
    else:
        
        clasificaciones = Clasificacion.objects.all().order_by('nombre')
        generos = Genero.objects.all().order_by('nombre')
        
        contexto = {
            'pelicula': pelicula,
            'clasificaciones': clasificaciones,
            'generos': generos,
        }
        
        return render(request, 'peliculas/editar.html', context=contexto)


def eliminarPelicula(request, pk):
    
    pelicula = get_object_or_404(Pelicula, pk=pk)
    
    if request.method == 'POST':
        pelicula.delete()
        return redirect('listarPeliculas')
    else:
        
        contexto = {
            'pelicula': pelicula,
        }
        
        return render(request, 'peliculas/eliminar.html', context=contexto)
