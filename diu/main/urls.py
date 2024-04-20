from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

# Aqui creamos las urls pa la aplicación
urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    re_path(r'^signin/$', views.Sign_in.as_view(), name='signin'),
    path('logout/', views.logout_user, name='logout'),
    path("notas/crear-nota", views.crearNota),
    path('notas/eliminar-nota/<int:nota_id>/', views.eliminarNota, name='eliminarNota'),
    path('notas/<int:nota_id>/', views.obtenerNota, name='obtenerNota'),
    path('notas/editar/<int:nota_id>/', views.editarNota, name='editarNota'),
    path('notas/filtrar/', views.filtrarNotas, name='filtrarNotas'),
    path('notas/filtrar/notas/editar/<int:nota_id>/', views.editarNota, name='editarNota'),
    path('notas/filtrar/notas/eliminar-nota/<int:nota_id>/', views.eliminarNota, name='eliminarNota')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
