#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Wednesday, March 30th 2016, 5:56:24 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Friday, April 15th 2016, 11:03:01 am

from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^vraspiapp/$',views.home),
    # login
    url(r'^vraspiapp/login/$', login,
    {
        'template_name': 'vraspiapp/login.html'
    }),
    # logout
    url(r'^vraspiapp/logout/$', logout,
    {
        'template_name': 'vraspiapp/logout.html'
    }),
    url(r'^vraspiapp/homemonitor$',views.homemonitor),
    url(r'^vraspiapp/signup/$', views.signup),
    url(r'^vraspiapp/signup_success/$', views.signup_success)
    # url(r'^vraspiapp/fetch_pic/$', views.fetch_pic)
]
