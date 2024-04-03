from django.shortcuts import render
from django.http import HttpResponse
from main.models import Color
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(req):
    return render(req, 'index.html')

def login(req):
    return render(req, 'login/login.html')

def color(response, id):
    return HttpResponse("<h1> %s </h1>" % Color.objects.get(id=id))