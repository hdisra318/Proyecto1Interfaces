from django.db import models
from django.contrib.auth.models import User, AbstractUser
import datetime

# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    fechaCreacion = models.DateField(default=datetime.date.today)
    correo = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        ordering = ["nombre"]


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
