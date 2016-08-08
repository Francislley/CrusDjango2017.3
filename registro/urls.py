#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from registro import views

urlpatterns = patterns('',
  url(r'^$', views.Login, name='login'),
  url(r'^index$', views.Index, name='index'),
  url(r'^consultar$', views.Consultar, name='consultar'),
  url(r'^crear_usuario$', views.Crear_usuario, name='crear_usuario'),
  url(r'^registrar$', views.Registrar, name='registrar'),
  url(r'^registro_exitoso$', views.Registro_exitoso, name='registro_exitoso'),
  url(r'^logout$', views.Logout, name='logout'),
  url(r'^editar/(?P<pk>\d+)$', views.Editar, name='editar'),
  url(r'^borrar/(?P<pk>\d+)$', views.Borrar, name='borrar'),
)