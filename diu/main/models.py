from django.db import models
from django.contrib.auth.models import User
import datetime


# Modelo Usuario
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1, null=False, blank=False)
    fechaCreacion = models.DateField(User, default=datetime.date.today)
    tipo = models.IntegerField(User, default=2)

    class Meta:
        ordering = ["user__first_name"]


# Modelo Fuente
class Fuente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        ordering = ["nombre"]

# Modelo Nota
class Nota(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    contenido = models.TextField(max_length=200)
    color = models.CharField(max_length=20)
    imagen = models.ImageField(null=True)
    fechaCreacion = models.DateField(default=datetime.date.today)
    fuente = models.ForeignKey(Fuente, on_delete=models.CASCADE, null=True)
    autores = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.titulo
    
    class Meta:
        ordering = ["titulo"]
