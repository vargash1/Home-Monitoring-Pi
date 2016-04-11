#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Wednesday, March 30th 2016, 6:13:47 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 4:46:12 am
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from forms import UserForm
from django.contrib.auth.models import User
from django.template import Template, Context
import mimetypes
import os
import time
from vraspi import listener

def home(request):
    return render(request, "vraspiapp/index.html", {})

def login_view(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'vraspiapp/login.html',c)

def loggedin(request):
    return render(request,'vraspiapp/loggedin.html')

def logout(request):
    return render(request, 'vraspiapp/logout.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            return render(request, 'vraspiapp/signup_success.html')
    else:
        form = UserForm()

    return render(request, 'vraspiapp/signup.html', {'form': form})

def signup_success(request):
    return render(request, 'vraspiapp/signup_success.html')

def homemonitor(request):
    listener = SensorListener(queue)
    listener.execute()
    while True:
        time.sleep(1)
        return render(request,"vraspiapp/homemonitor.html")
