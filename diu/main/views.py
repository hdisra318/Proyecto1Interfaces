from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistroUsuarioForm, NotaForm
from .models import Nota, Usuario, Fuente

# Create your views here.
@login_required(login_url='/login')
def home(req):
    user_authenticated = req.user.is_authenticated
    notas = Nota.objects.all()
    return render(req, 'home.html', {'username': req.user ,'user_authenticated': user_authenticated, 'notas': notas})

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
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NotaForm()
    return render(req, 'notas/crearNota.html', {'user_authenticated': user_authenticated, 'autores': autores, 'fuentes': fuentes,'form': form})

# def color(response, id):
#     return HttpResponse("<h1> %s </h1>" % Color.objects.get(id=id))
