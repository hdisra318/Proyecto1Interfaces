from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

# Aqui creamos las urls pa la aplicación
urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("signin/", views.signin, name="signin"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path("notas/crear-nota", views.crearNota),
    path('notas/eliminar-nota/<int:nota_id>/', views.eliminarNota, name='eliminarNota'),
    path('notas/<int:nota_id>/', views.obtenerNota, name='obtenerNota'),
    path('notas/editar/<int:nota_id>/', views.editarNota, name='editarNota'),
    # path("color/<int:id>", views.color, name="color"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)