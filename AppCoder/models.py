from django.db import models


# Create your models here.

class Datos_Familiar(models.Model):
    
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Edad = models.IntegerField()
    Fecha_Carga = models.DateField()
   
