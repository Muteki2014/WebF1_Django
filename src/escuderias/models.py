from django.db import models

# Create your models here.

class Escuderia(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    jefe_equipo = models.CharField(max_length=100)
    puntos = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    foto = models.ImageField(upload_to='escuderias/', blank=True, null=True)
    

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['nombre']