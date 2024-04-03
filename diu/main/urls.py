from django.urls import path
from . import views

# Aqui creamos las urls pa la aplicación
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("color/<int:id>", views.color, name="color"),
]