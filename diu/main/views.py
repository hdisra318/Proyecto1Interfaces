from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistroUsuarioForm, NotaForm
from .models import Nota, Usuario, Fuente
from django.views.generic import CreateView
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login')
def home(req):
    user_authenticated = req.user.is_authenticated
    notas = Nota.objects.all()
    autores = User.objects.all()
    fuentes = Fuente.objects.all()

    return render(req, 'home.html', {'username': req.user ,'user_authenticated': user_authenticated, 'notas': notas, 'autores': autores, 'fuentes': fuentes})

# Login de usuarios
def login_user(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        print(user)
        if user is not None:
            login(req, user)

            user_authenticated = req.user.is_authenticated
            return render(req, 'home.html', {'user_authenticated': user_authenticated})

        
        else:
            messages.error(req, 'Ups!, El nombre de usuario o la contraseña son incorrectas')
    
    return render(req, 'login/login.html')


# Registro de usuarios
class Sign_in(CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = 'main/signin.html'

    def form_valid(self, form):
        '''
        En esta parte, si el form es valido lo guardamos y usamos authenticate e iniciamos sesión
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')


def logout_user(req):
    logout(req)

    return redirect('/login')

@login_required(login_url='/login')
def crearNota(req):
    user_authenticated = req.user.is_authenticated
    autores = User.objects.all()
    fuentes = Fuente.objects.all()

    if req.method == 'POST':
        form = NotaForm(req.POST, req.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.error(req, "Ups!, ¡Verifique los campos!")
    else:
        form = NotaForm()
        

    return render(req, 'notas/crearNota.html', {'user_authenticated': user_authenticated, 'autores': autores, 'fuentes': fuentes,'form': form})


# Edita la nota
@login_required(login_url='/login')
def editarNota(req, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    
    if req.method == 'POST':
        form = NotaForm(req.POST, req.FILES, instance=nota)
        if form.is_valid():
            form.save()
    
    return redirect('/')


# Elimina la nota dada de la base de datos
def eliminarNota(req, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)

    if req.method == 'POST':
        nota.delete()
    
        return  JsonResponse({'mensaje': 'La nota ha sido eliminada correctamente'})
    
    return  JsonResponse({'error': 'Ocurrio un error al eliminar la nota'})


# Obtiene la informacion de la nota de la base de datos
@login_required(login_url='/login')
def obtenerNota(req, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    
    autores = [{'id': autor.id, 'username': autor.username} for autor in nota.autores.all()]

    data = {
        'id': nota.id,
        'titulo': nota.titulo,
        'contenido': nota.contenido,
        'color': nota.color,
        'imagen': nota.imagen.url,
        'fecha_creacion': nota.fechaCreacion.strftime('%Y-%m-%d'),
        'fuente': nota.fuente.nombre if nota.fuente else None,
        'autores': autores
    }

    return JsonResponse(data)