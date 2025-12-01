from django.db import models

# Create your models here.


class Circuito(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    longitud_km = models.DecimalField(max_digits=5, decimal_places=2, help_text="Longitud en kilómetros")
    vueltas = models.PositiveIntegerField(default=0)
    record_vuelta = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    foto = models.ImageField(upload_to='circuitos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.pais})"
    
    
    class Meta:
        ordering = ['pais', 'nombre']
        

