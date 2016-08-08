#Registro de participantes de un congreso - Vistas basadas en funciones

Creado por dM

##Versiones
```
Django==1.8.8
Python==2.7
```

##(Registrar Persona)

Aplicación que sirve para registrar
personas, almacenar los registros en
una base de datos y luego consultar
los mismos. Se veran ejemplos sencillos
de creación de modelos, vistas basadas
en funciones y la utilización de etiquetas
con codigo python en las plantillas.

##Tip

1)La base de datos es sqlite3, al
migrar se creara, así como
creara la tabla y campos descritos
en el modelo.

2)Incorpora sistema de autenticacion de usuarios y creación de cuentas de usuario.

##Comandos usados en secuencia para probar el proyecto

$ python manage.py migrate

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py createsuperuser

$ python manage.py runserver
