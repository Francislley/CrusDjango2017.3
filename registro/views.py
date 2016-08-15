#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from registro.forms import MyRegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from registro.models import Persona
from django.forms import ModelForm
from django.contrib import auth



class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre','apellido','cedula','tlf','ocupacion',]



'''
Función que valida si un usuario está autenticado, si no está autenticado
se muestra el formulario de logeo.
'''
def Login(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/index')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                #if acceso.is_staff:
                    login(request, acceso)
                    return HttpResponseRedirect('index')
                else:
                    return render_to_response('registro/usuario_no_activo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('registro/no_es_usuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('registro/login.html',{'formulario':formulario}, context_instance=RequestContext(request))



'''
Función que permite crear usuarios, si la cuenta se creo con éxito
se redirige a otra plantilla.
'''
def Crear_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            nuevo_usuario = form.save()
            #return render_to_response('registro/registro_exitoso.html', context_instance=RequestContext(request))
            return HttpResponseRedirect('/registro_exitoso')
        else:
            return HttpResponseRedirect('registro/index')
    args = {}
    args['form'] = MyRegistrationForm()
    #return render_to_response('registro/crear_usuario.html', {'args':args}, context_instance=RequestContext(request))
    return render(request, 'registro/crear_usuario.html', args)



'''
Vista de la plantilla principal, accede a esta luego de iniciar sesión.
'''
@login_required(login_url='/')
def Index(request):
    usuario = request.user
    return render_to_response('registro/index.html', {'usuario':usuario}, context_instance=RequestContext(request))



'''
Vista de la plantilla para consultar participantes registrados del congreso.
'''
@login_required(login_url='/')
def Consultar(request, template_name='registro/consultar.html'):
    persona = Persona.objects.all()
    data = {}
    data['object_list'] = persona
    return render(request, template_name, data)



'''
Vista de la plantilla para registrar participantes del congreso.
'''
@login_required(login_url='/')
def Registrar(request, template_name='registro/registrar.html'):
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('registro:consultar')
    return render(request, template_name, {'form':form})



'''
Vista de la plantilla para editar los datos de los participantes del congreso.
'''
@login_required(login_url='/')
def Editar(request, pk, template_name='registro/registrar.html'):
    persona= get_object_or_404(Persona, pk=pk)
    form = PersonaForm(request.POST or None, instance=persona)
    if form.is_valid():
        form.save()
        return redirect('registro:consultar')
    return render(request, template_name, {'form':form})



'''
Vista de la plantilla para eliminar participantes del congreso.
'''
@login_required(login_url='/')
def Borrar(request, pk, template_name='registro/borrar.html'):
    persona= get_object_or_404(Persona, pk=pk)    
    if request.method=='POST':
        persona.delete()
        return redirect('registro:consultar')
    return render(request, template_name, {'object':persona})



'''
Funcion que cierra la sesión del usuario.
'''
@login_required(login_url='/')
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')



'''
Vista de la plantilla que se muestra cuando la cuenta de usuario se creó correctamente.
'''
def Registro_exitoso(request):
    usuario = request.user
    return render_to_response('registro/registro_exitoso.html', {'usuario':usuario}, context_instance=RequestContext(request))



'''
Vista de la plantilla que se muestra el formulario para cambiar la contraseña de la cuenta creada.
'''
@login_required(login_url='/')
def Cambiar_contrasena(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cambio_de_contrasena_exitoso')
        else:
            return HttpResponseRedirect('/cambiar_contrasena')
    return render(request, 'registro/cambiar_contrasena_usuario.html', {'form': form,})



'''
Vista de la plantilla que muestra mensaje de cambio de contraseña exitoso.
'''
@login_required(login_url='/')
def Cambio_de_contrasena_exitoso(request):
    usuario = request.user
    return render_to_response('registro/cambio_de_contrasena_exitoso.html', {'usuario':usuario}, context_instance=RequestContext(request))



'''
Vista de la plantilla que muestra el perfil del usuario autenticado.
'''
@login_required(login_url='/')
def Perfil(request):
    usuario = request.user
    return render_to_response('registro/perfil.html', {'usuario':usuario}, context_instance=RequestContext(request))