from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Aqui creamos las urls pa la aplicación
urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("signin/", views.signin, name="signin"),
    path("notas/crear-nota", views.crearNota),
    # path("color/<int:id>", views.color, name="color"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)