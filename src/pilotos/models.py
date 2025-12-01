from django.db import models

# Create your models here.

class Piloto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    numero = models.PositiveIntegerField(unique=True)
    escuderia = models.CharField(max_length=100, blank=True, null=True)
    puntos = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    
    foto = models.ImageField(upload_to='pilotos/', blank=True, null=True)
    

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.numero})"
    
    class Meta:
        ordering = ['apellido', 'nombre']
        


