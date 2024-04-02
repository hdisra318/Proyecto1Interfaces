from django.db import models

# Create your models here.

class Color(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    hexadecimal = models.CharField(max_length=6, unique = True)
    
    def __str__(self) -> str:
        return self.nombre

class Nota(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=200)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    #imagen la agrego si lo hacemos xd

    def __str__(self) -> str:
        return self.titulo