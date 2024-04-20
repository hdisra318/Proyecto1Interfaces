from django.http import HttpResponseRedirect
from django.urls import reverse

class RedirectIfAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        # Rutas a aplicar el middleware
        self.redirect_paths = ['/login/', '/signin/']

    def __call__(self, request):
        # Verifica si el usuario esta autenticado y si la ruta solicitada está en la lista de rutas de redireccion
        if request.user.is_authenticated and request.path_info in self.redirect_paths:
            # Redirige al usuario a la página principal (home)
            return HttpResponseRedirect(reverse('home'))
        
        
        response = self.get_response(request)
        return response
