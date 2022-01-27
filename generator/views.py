from django.shortcuts import render
from django.http import HttpResponse
import random

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characthers = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characthers.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characthers.extend(list('1234567890'))
    if request.GET.get('special'):
        characthers.extend(list('!@_#$%^&*()'))

    for i in range(length):
        generated_password += random.choice(characthers)
        

    return render(request, 'generator/password.html', {'password': generated_password})