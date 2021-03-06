#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Wednesday, March 30th 2016, 6:13:47 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Friday, April 15th 2016, 10:45:30 am
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
from multiprocessing import Queue
import mimetypes
import json
import os
import time
from vraspi import listener, log
vlog = log.VRaspLog()
vlog.initLogger()

queue = Queue()
global queue
listnr = listener.SensorListener(vlog, queue)
listnr.execute()

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

def get_data():
    return HttpResponse("lel")

def email_event():
    title = "vRaspi Notify"
    tmp = "Motion sensor AND ultrasonic sensor both triggered. Possible Intruder!"
    send_mail(title,tmp,settings.EMAIL_HOST_USER, ['arithmosbot@gmail.com'],fail_silently=False)
    vlog.logInfo("Send Email!")

# def fetch_pic(request):
#     filepath = tmpcam.take_Pic()
#     with open(filepath,'rb') as f:
#         datain = f.read()
#     response = HttpResponse(datain, content_type=mimetypes.guess_type(filepath)[0])
#     response['Content-Disposition'] = "attachment; filename={0}".format(filepath)
#     response['Content-Length'] = os.path.getsize(filepath)
#     return response

def homemonitor(request):
    data = []
    trigger1 = False
    trigger2 = False
    for i in range(queue.qsize()):
        # As we read messages, they will be popped off
        msg = listnr.getQueueMessage()
        if msg is not None:
            data.append(msg)
        for elem in msg:
            if elem == "motion":
                trigger1 = True
            if elem == "ultra":
                trigger2 = True
    # Only upon Motion sensor and Ultrasonic sensor triggering
    # Send an email
    if trigger1 and trigger2:
        email_event()

    housetemp = listnr.getTempReading()
    return render(request, 'vraspiapp/homemonitor.html', {'data':data,"housetemp":housetemp})
