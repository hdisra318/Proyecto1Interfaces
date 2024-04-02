from django.urls import path
from . import views

# Aqui creamos las urls pa la aplicación
urlpatterns = [
    path("", views.index, name="index"),
    path("color/<int:id>", views.color, name="color"),
]