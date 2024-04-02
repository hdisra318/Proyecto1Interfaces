from django.shortcuts import render
from django.http import HttpResponse
from main.models import Color

# Create your views here.
def index(response):
    return HttpResponse("<h1> Hola Mundo </h1>")

def color(response, id):
    return HttpResponse("<h1> %s </h1>" % Color.objects.get(id=id))