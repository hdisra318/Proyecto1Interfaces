from django import forms
from .models import Usuario, Nota
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):

    nombre = forms.CharField(max_length=50)
    correo = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'password1', 'password2']


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo', 'contenido', 'color', 'imagen', 'fuente', 'autores']