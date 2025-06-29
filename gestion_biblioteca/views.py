from django.shortcuts import render, redirect
from .forms import AutorForm, LibroForm, LectorForm, PrestamoForm
from .models import Autor, Libro, Lector


def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_autor')
    else:
        form = AutorForm()
    return render(request, 'gestion_biblioteca/agregar_autor.html', {'form': form})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_libro')
    else:
        form = LibroForm()
    return render(request, 'gestion_biblioteca/agregar_libro.html', {'form': form})

def agregar_lector(request):
    if request.method == 'POST':
        form = LectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_lector')
    else:
        form = LectorForm()
    return render(request, 'gestion_biblioteca/agregar_lector.html', {'form': form})

def agregar_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            return redirect('lista_libros')
    else:
        form = PrestamoForm()
        return render(request, 'gestion_biblioteca/agregar_prestamo.html', {'form': form})


def inicio(request):
    return render(request, 'gestion_biblioteca/inicio.html')

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'gestion_biblioteca/lista_autores.html', {'autores': autores})

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'gestion_biblioteca/lista_libros.html', {'libros': libros})

def lista_lectores(request):
    lectores = Lector.objects.all()
    return render(request, 'gestion_biblioteca/lista_lectores.html', {'lectores': lectores})
  