from django.db import models
import datetime

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=20)
    fechaCreacion = models.DateField(default=datetime.date.today)
    tipo = models.IntegerField(null=True)
    correo = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        ordering = ["username"]


class Fuente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, unique=True)
    url = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        ordering = ["nombre"]

class Nota(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    contenido = models.TextField(max_length=200)
    color = models.CharField(max_length=20)
    imagen = models.ImageField(null=True)
    fechaCreacion = models.DateField(default=datetime.date.today)
    fuente = models.ForeignKey(Fuente, on_delete=models.CASCADE, null=True)
    autores = models.ManyToManyField(Usuario)

    def __str__(self) -> str:
        return self.titulo
    
    class Meta:
        ordering = ["titulo"]
