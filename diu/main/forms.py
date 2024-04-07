from django import forms
from .models import Usuario, Nota

class RegistroUsuarioForm(forms.ModelForm):
    contrasena_confirmacion = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'correo', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get("contrasena")
        # contrasena_confirmacion = cleaned_data.get("contrasena_confirmacion")
        # if contrasena != contrasena_confirmacion:
        #     raise forms.ValidationError("Las contraseñas no coinciden")


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo', 'contenido', 'color', 'imagen', 'fuente', 'autores']