# Proyecto 1 del curso de Diseño de Interfaces de Usuario

## Integrantes
- Israel Hernández Dorantes
- Marco Antonio
- Diego Calzada
- Kevin Jair
- Kassandra Mirael
- Camila Cruz

## Instrucciones para ejecutar este pedo
- Crear un entorno virtual con el comando `python -m venv .env`
 
- Activar el entorno virtual `.env`.
- Para windows usar el comando: `.env\Scripts\activate.bat`.
- Para algunos linux y mac `source .env/Scripts/activate`
- En Fedora `source .env/bin/activate`

- Para salir del entorno virtual: `> deactivate`
- Instalar las bibliotecas de `django` y `pillow` con los comandos:
```
pip install django
pip install Pillow
pip install django-extensions
```

- Una vez activado ir al directorio `diu/`

- Ejecutar el comando
```python manage.py runserver```

- En caso de ser necesario usar el comando `python manage.py migrate` y el comando `python manage.py makemigrations main`
- En caso de que no se efectuen las migraciones de manera correcta eliminar la base de datos y hacer los pasos del punto anterior


## Pruebas

Si se requieren hacer registros en la base de datos para probarlos los ejemplos son los siguientes:

Ejecutas `python manage.py shell` para abrir una shell con python

### Agregando Fuentes
```
from main.model import Usuario, Fuente, Nota

f = Fuente(nombre="Ejemplo",url="link") # Creando objeto
f.save() # Guardando objeto
Fuente.objects.all() #Viendo todos los objetos de la tabla
```
### Agregando Usuarios
```
from main.model import Usuario, Fuente, Nota
import datetime
u = Usuario(username="DONMARCORS",nombre="Marco",contrasena="hola",fechaCreacion=datetime.date(2024,4,4),tipo=1,correo="marcoantonioriverasilva@ciencias.unam.mx") # Creando objeto
u.save() # Guardando objeto
Usuario.objects.all() #Viendo todos los objetos de la tabla
```
### Agregando Notas
```
from main.model import Usuario, Fuente, Nota
import datetime
n = Nota(titulo="Nota 1", contenido="Hola Diego",color="rojo",imagen=None,fechaCreacion=datetime.date(2024,4,4), fuente=Fuente(Fuente.objects.get(id=1).id)) # crea la nota
n.save() # guarda la nota
Nota.objects.all() # mUestra todas las notas
Nota.objects.get(id=1).autores.set(Usuario.objects.all()) # asigna como autores a todos alv
```
# Sistemas Operativos donde funciona
Por el momento el unico Sistema Operativo donde no funciona correctamente es sobre MacOs
