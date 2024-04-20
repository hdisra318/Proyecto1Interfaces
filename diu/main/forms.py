from django import forms
from .models import Nota
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistroUsuarioForm(UserCreationForm):

    first_name = forms.CharField(max_length=140, required=True, widget=forms.TextInput(attrs={'id': 'first_name', 'class': 'form-control','name':'first_name'}))
    username = forms.CharField(max_length=140, required=True, widget=forms.TextInput(attrs={'id': 'id_username', 'class': 'form-control', 'name': 'username'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'id': 'email', 'class': 'form-control','name':'email', 'type': 'email'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'id': 'id_password1', 'class': 'form-control','name':'password1'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'id': 'id_password2', 'class': 'form-control','name':'password2'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'password1',
            'password2',
        )

    def username_clean(self):   
        username = self.cleaned_data['username'].lower()   
        new = User.objects.filter(username = username)   
        if new.count():   
            raise ValidationError("El usuario ya existe")   
        return username   
   
    def email_clean(self):   
        email = self.cleaned_data['email'].lower()   
        new = User.objects.filter(email=email)   
        if new.count():   
            raise ValidationError("El e-mail introdiucido ya existe")   
        return email   
   
    def clean_password(self):   
        password1 = self.cleaned_data['password1']   
        password2 = self.cleaned_data['password2']   
   
        if password1 and password2 and password1 != password2:   
            raise ValidationError("Las contraseñas no coinciden")   
        return password1   
   
    def save(self, commit = True):   
        user = User.objects.create_user(   
            self.cleaned_data['username'],   
            self.cleaned_data['email'],   
            self.cleaned_data['password1']   
        )   
        return user


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo', 'contenido', 'color', 'imagen', 'fuente', 'autores']


class FiltroNotasForm(forms.Form):
    titulo = forms.CharField(required=False, label='Título', widget=forms.TextInput(attrs={'id': 'filtro-titulo', 'name':'filtro-titulo', 'class': 'form-control', 'type': 'text', 'placeholder': 'Título de la nota'}))
    color = forms.CharField(required=False, label='Color', widget=forms.TextInput(attrs={'type': 'color', 'id': 'filtro-color', 'name':'filtro-color', 'class': 'form-control form-control-color', 'style': 'border-radius: 50%; border: none;'}))
    fecha_creacion = forms.DateField(required=False, label='Fecha de Creación', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))