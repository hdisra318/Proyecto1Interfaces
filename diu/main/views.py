from django.shortcuts import render
from django.http import HttpResponse
from main.models import Color
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def home(req):
    user_authenticated = req.user.is_authenticated
    return render(req, 'home.html', {'user_authenticated': user_authenticated})

def login(req):
    return render(req, 'login/login.html')

def signin(req):
    return render(req, 'signin/signin.html')

@login_required(login_url='/login')
def crearNota(req):
    user_authenticated = req.user.is_authenticated
    return render(req, 'notas/crearNota.html', {'user_authenticated': user_authenticated})

def color(response, id):
    return HttpResponse("<h1> %s </h1>" % Color.objects.get(id=id))