# -*- coding: utf-8 -*-
__author__ = 'caokun'
__date__ = '2019/7/22 17:24'

from django.urls import path
from . import views

urlpatterns = [
    path('publish/',views.publish,name='发布页面'),
    path('success/',views.success,name='发布成功'),
]
