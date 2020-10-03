#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-01-06 00:11:27
# @Last Modified by:   Sahil Dua
# @Last Modified time: 2016-08-10 23:58:19

#from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'hackIDE'

urlpatterns = [
    path('', views.index, name='index'),
    path('compile/', views.compileCode, name='compile'),
    path('run/', views.runCode, name='run'),
    path('code_id=<code_id>/', views.savedCodeView, name='saved-code'),
]
