# Proyecto 1 del curso de Diseño de Interfaces de Usuario

## Integrantes
- Israel Hernández Dorantes
- Marco Antonio Rivera
- Diego Calzada
- Kevin Jair
- Kassandra Mirael
- Camila Cruz

## Instrucciones para ejecutar la aplicación
- Activar el entorno virtual:
> Para windows usar el comando: `> entorno_virtual/Scripts/activate`

> Para linux y mac `source .env/Scripts/activate`

- Para salir del entorno virtual: `> deactivate`
  
- Instalar las bibliotecas de `django` y `pillow` con los comandos:
```
pip install django
pip install Pillow
```

- Una vez activado ir al directorio `diu/`

- Ejecutar el comando
```python manage.py runserver```

- En caso de ser necesario usar el comando `python manage.py makemigrations` y el comando `python manage.py migrate`.
- En caso de que no se efectuen las migraciones de manera correcta eliminar la base de datos y hacer los pasos del punto anterior
