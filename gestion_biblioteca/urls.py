from django.urls import path
from . import views

urlpatterns = [
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('agregar_lector/', views.agregar_lector, name='agregar_lector'),
    path('agregar_prestamo/', views.agregar_prestamo, name='agregar_prestamo'),

    path('', views.inicio, name='inicio'),
    path('autores/', views.lista_autores, name='lista_autores'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('lectores/', views.lista_lectores, name='lista_lectores')
]