from django import forms
from .models import Usuario, Nota

class RegistroUsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'correo', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo', 'contenido', 'color', 'imagen', 'fuente', 'autores']