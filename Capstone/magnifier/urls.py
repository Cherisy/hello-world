#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Jiexun Li'

from django.urls import path
from . import views

app_name = 'magnifier'

urlpatterns=[
    path('', views.index, name='index'),
    path('result/', views.upload_image, name = 'result'),
]