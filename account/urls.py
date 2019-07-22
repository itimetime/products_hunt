# -*- coding: utf-8 -*-
__author__ = 'caokun'
__date__ = '2019/7/22 9:38'

from . import views
from django.urls import path


urlpatterns = [

    path('sign',views.signup,name='注册页面'),
    path('login',views.login,name='登录'),
    path('logout',views.logout,name='登出')
    ]
