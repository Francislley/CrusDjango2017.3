#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
#from django.contrib.auth.decorators import login_required

from registro import views

urlpatterns = patterns('',
  url(r'^$', views.Login, name='login'),
  url(r'^index$', views.Index, name='index'),
  url(r'^consultar$', views.Consultar, name='consultar'),
  url(r'^crear_usuario$', views.Crear_usuario, name='crear_usuario'),
  url(r'^registrar$', views.Registrar, name='registrar'),
  url(r'^registro_exitoso$', views.Registro_exitoso, name='registro_exitoso'),
  url(r'^cambiar_contrasena/$',views.Cambiar_contrasena, name='cambiar_contrasena'),
  url(r'^cambio_de_contrasena_exitoso/$',views.Cambio_de_contrasena_exitoso, name='cambio_de_contrasena_exitoso'),
  url(r'^logout$', views.Logout, name='logout'),
  url(r'^editar/(?P<pk>\d+)$', views.Editar, name='editar'),
  url(r'^borrar/(?P<pk>\d+)$', views.Borrar, name='borrar'),
  url(r'^perfil$', views.Perfil, name='perfil'),
  #url(r"^xxxxx/$", view=login_required(Vista_basada_en_Clase.as_view()), name="Vista_basada_en_Clase"),
)