from django.db import models

class Autor(models.Model):
    nombre_completo = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __star__(self):
        return self.nombre_completo

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.CharField(max_length=100)
    sinopsis = models.TextField()

    def __str__(self):
        return self.titulo
    
class Lector(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    libros_prestados = models.ManyToManyField(Libro, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.libro.titulo} prestado a {self.lector.nombre} {self.lector.apellido}"

