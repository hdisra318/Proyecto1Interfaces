from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistroUsuarioForm, NotaForm
from .models import Nota, Usuario, Fuente
from django.core import serializers
from django.views.decorators.http import require_http_methods
import json

# Create your views here.
@login_required(login_url='/login')
def home(req):
    user_authenticated = req.user.is_authenticated
    notas = Nota.objects.all()
    autores = Usuario.objects.all()
    fuentes = Fuente.objects.all()

    return render(req, 'home.html', {'username': req.user ,'user_authenticated': user_authenticated, 'notas': notas, 'autores': autores, 'fuentes': fuentes})

# Login de usuarios
def login_user(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(req, user)

            user_authenticated = req.user.is_authenticated
            return render(req, 'home.html', {'user_authenticated': user_authenticated})

        
        else:
             messages.error(req, 'Ups!, El nombre de usuario o la contraseña son incorrectas')
    
    return render(req, 'login/login.html')

# Registro de usuarios
def signin(req):
    if req.method == 'POST':
        
        form = RegistroUsuarioForm(req.POST)

        print(form)
        if form.is_valid():
            form.save()
            return redirect('/') 

        else:
            form = RegistroUsuarioForm()
        

    return render(req, 'signin/signin.html')


@login_required(login_url='/login')
def crearNota(req):
    user_authenticated = req.user.is_authenticated
    autores = Usuario.objects.all()
    fuentes = Fuente.objects.all()

    if req.method == 'POST':
        form = NotaForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NotaForm()
    return render(req, 'notas/crearNota.html', {'user_authenticated': user_authenticated, 'autores': autores, 'fuentes': fuentes,'form': form})


# Edita la nota
@login_required(login_url='/login')
def editarNota(req, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    
    if req.method == 'POST':
        form = NotaForm(req.POST, req.FILES, instance=nota)
        if form.is_valid():
            form.save()
    
    return redirect('/')


# Elimina la nota dada de la base de datos
def eliminarNota(req, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)

    if req.method == 'POST':
        nota.delete()
    
        return  JsonResponse({'mensaje': 'La nota ha sido eliminada correctamente'})
    
    return  JsonResponse({'error': 'Ocurrio un error al eliminar la nota'})


# Obtiene la informacion de la nota de la base de datos
@login_required(login_url='/login')
def obtenerNota(req, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    data = {
        'id': nota.id,
        'titulo': nota.titulo,
        'contenido': nota.contenido,
        'color': nota.color,
        'imagen': nota.imagen.url,
        'fecha_creacion': nota.fechaCreacion.strftime('%Y-%m-%d'),
        'fuente': nota.fuente.nombre if nota.fuente else None,
        'autores': [autor.nombre for autor in nota.autores.all()]
    }

    return JsonResponse(data)
