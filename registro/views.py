#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.http import HttpResponseRedirect
#Authentication libs
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.template import RequestContext
from registro.forms import MyRegistrationForm
from django.contrib import auth

from registro.models import Persona

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre','apellido','cedula','tlf','ocupacion',]



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
                #if acceso.is_active:
                if acceso.is_staff:
                    login(request, acceso)
                    return HttpResponseRedirect('index')
                else:
                    return render_to_response('registro/usuario_no_activo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('registro/no_es_usuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('registro/login.html',{'formulario':formulario}, context_instance=RequestContext(request))



@login_required(login_url='/')
def Index(request):
    usuario = request.user
    return render_to_response('registro/index.html', {'usuario':usuario}, context_instance=RequestContext(request))



@login_required(login_url='/')
def Consultar(request, template_name='registro/consultar.html'):
    persona = Persona.objects.all()
    data = {}
    data['object_list'] = persona
    return render(request, template_name, data)


@login_required(login_url='/')
def Registrar(request, template_name='registro/registrar.html'):
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('registro:consultar')
    return render(request, template_name, {'form':form})


@login_required(login_url='/')
def Editar(request, pk, template_name='registro/registrar.html'):
    persona= get_object_or_404(Persona, pk=pk)
    form = PersonaForm(request.POST or None, instance=persona)
    if form.is_valid():
        form.save()
        return redirect('registro:consultar')
    return render(request, template_name, {'form':form})


@login_required(login_url='/')
def Borrar(request, pk, template_name='registro/borrar.html'):
    persona= get_object_or_404(Persona, pk=pk)    
    if request.method=='POST':
        persona.delete()
        return redirect('registro:consultar')
    return render(request, template_name, {'object':persona})
