from django import forms
from .models import Autor, Libro, Lector, Prestamo

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre_completo', 'nacionalidad']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero', 'sinopsis']

class LectorForm(forms.ModelForm):
    class Meta:
        model = Lector
        fields = ['nombre', 'apellido', 'email', 'libros_prestados']

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro', 'lector']