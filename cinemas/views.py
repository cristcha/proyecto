from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import Cinema, Sala, Formato, MapaSala
import json



# Administración Cinemas

def listarCinemas(request):
    
    cinemas = Cinema.objects.annotate(cantidad_salas=Count('sala'))
    
    contexto = {
        'cinemas': cinemas,
    }
    
    return render(request, 'cinemas/listar.html', context=contexto)


def agregarCinema(request):

    if request.method == 'POST':
        
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        
        Cinema.objects.create(nombre=nombre, direccion=direccion)

        return redirect('listarCinemas')
    
    else:
        return render(request, 'cinemas/agregar.html')


def editarCinema(request, pk):

    cinema = get_object_or_404(Cinema, pk=pk)
    
    if request.method == 'POST':
        
        cinema.nombre = request.POST['nombre']
        cinema.direccion = request.POST['direccion']
        cinema.save()
        
        return redirect('listarCinemas')
        
    else:
    
        
        contexto = {
            'cinema': cinema,
        }
        
        return render(request, 'cinemas/editar.html', context=contexto)

def eliminarCinema(request, pk):

    cinema = get_object_or_404(Cinema, pk=pk)
    
    if request.method == 'POST':
        
        cinema.delete()
        
        return redirect('listarCinemas')
        
    else:
    
        
        contexto = {
            'cinema': cinema,
        }
        
        return render(request, 'cinemas/eliminar.html', context=contexto)

# Administración Salas

def listarSalas(request):
    
    salas = Sala.objects.all()
    
    contexto = {
        'salas': salas,
    }
    
    return render(request, 'salas/listar.html', context=contexto)

def agregarSala(request):
    if request.method == 'POST':
        
        nombre = request.POST['nombre']
        capacidad = request.POST['capacidad']
        # Por defecto guardar el estado como 1 (Abierta)
        estado = 1
        
        formato = request.POST['formato']
        formato = get_object_or_404(Formato, pk=formato)
        
        cinema = request.POST['cinema']
        cinema = get_object_or_404(Cinema, pk=cinema)
        
        Sala.objects.create(nombre=nombre, capacidad=capacidad, estado=estado, id_formato=formato, id_cinema=cinema)
        
        return redirect('listarSalas')
        
    else:
        formatos = Formato.objects.all()
        cinemas = Cinema.objects.all()
        
        contexto = {
            'formatos': formatos,
            'cinemas': cinemas,
        }
        
        return render(request, 'salas/agregar.html', context=contexto)

def editarSala(request, pk):
    
    sala = get_object_or_404(Sala, pk=pk)
    
    if request.method == 'POST':
        
        # Validar cambios
        if request.POST['nombre'] != sala.nombre:
            sala.nombre = request.POST['nombre']
            
        if request.POST['capacidad'] != sala.capacidad:
            sala.capacidad = request.POST['capacidad']
            
        if request.POST['estado'] != sala.estado:
            sala.estado = request.POST['estado']
            
        if request.POST['formato'] != sala.id_formato:
            formato = request.POST['formato']
            sala.id_formato = get_object_or_404(Formato, pk=formato)

        if request.POST['cinema'] != sala.id_cinema:
            cinema = request.POST['cinema']
            sala.id_cinema = get_object_or_404(Cinema, pk=cinema)

        # Guardar cambios
        sala.save()
        
        return redirect('listarSalas')
    else:
        
        formatos = Formato.objects.all()
        cinemas = Cinema.objects.all()
        
        contexto = {
            'sala': sala,
            'formatos': formatos,
            'cinemas': cinemas,
        }
        
        return render(request, 'salas/editar.html', context=contexto)