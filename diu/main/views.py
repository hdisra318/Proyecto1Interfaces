from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
@login_required(login_url='/login')
def home(req):
    user_authenticated = req.user.is_authenticated
    return render(req, 'home.html', {'user_authenticated': user_authenticated})

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

def signin(req):
    return render(req, 'signin/signin.html')

@login_required(login_url='/login')
def crearNota(req):
    user_authenticated = req.user.is_authenticated
    return render(req, 'notas/crearNota.html', {'user_authenticated': user_authenticated})

# def color(response, id):
#     return HttpResponse("<h1> %s </h1>" % Color.objects.get(id=id))
