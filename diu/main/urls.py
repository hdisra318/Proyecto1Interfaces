from django.urls import path
from . import views

# Aqui creamos las urls pa la aplicación
urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("signin/", views.signin, name="signin"),
    path("notas/crear-nota", views.crearNota),
    # path("color/<int:id>", views.color, name="color"),
]