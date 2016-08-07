#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from registro import views

urlpatterns = patterns('',
  url(r'^$', views.Index, name='index'),
  url(r'^consultar$', views.Consultar, name='consultar'),
  url(r'^registrar$', views.Registrar, name='registrar'),
  url(r'^editar/(?P<pk>\d+)$', views.Editar, name='editar'),
  url(r'^borrar/(?P<pk>\d+)$', views.Borrar, name='borrar'),
)