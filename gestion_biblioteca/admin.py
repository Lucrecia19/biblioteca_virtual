from django.contrib import admin
from .models import Autor, Libro, Lector, Prestamo

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Lector)
admin.site.register(Prestamo)

