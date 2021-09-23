from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect ,HttpResponse
from django.contrib import messages
from .models import  Contact, Volunteer, Plant, Send
import re

# Create your views here.

def home(request):
    return render(request, 'et/home.html')

def team(request):
    return render(request, 'et/team.html')

def ourprojects(request):
    return render(request, 'et/ourprojects.html')

def about(request):
    return render(request, 'et/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('NAME')
        pattern = "^[A-Za-z_-]*$"
        state = bool(re.match(pattern, name))
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        message = request.POST.get('Message')
        print(name, email, phone, message)
        if state and len(phone)==10:
            contact = Contact(name=name, email=email, phone=phone, message=message)
            contact.save()
            return HttpResponse("Thanks for contacting")
        if not(state):
            return HttpResponse("Name should be character type")
        else:
            return HttpResponse("Phone no. should be of 10 digit")


    return render(request,'et/contact.html')


def volunteer(request):
    if request.method=='POST':
        name = request.POST['NAME']
        email = request.POST['Email']
        city = request.POST['CITY']
        help = request.POST.get('HELP')
        pattern = "^[A-Za-z_-]*$"
        state = bool(re.match(pattern, name))
        print(state)
        if state:
            volunteer = Volunteer(name=name, email=email, city=city, help=help)
            volunteer.save()
            return HttpResponse("Thanks for contacting")
        else:
            return HttpResponse("Name should be character type")

    return render(request,'et/home.html')

def plant(request):
    if request.method=='POST':
        name = request.POST.get('NAME')
        email = request.POST.get('Email')
        city = request.POST.get('City')
        pattern = "^[A-Za-z_-]*$"
        state = bool(re.match(pattern, name))
        print(state)
        if state:
            plant = Plant(name=name, email=email, city=city)
            plant.save()
            return HttpResponse("Thanks for contacting")
        else:
            return HttpResponse("Name should be character type")


    return render(request,'et/home.html')

def send(request):
    if request.method=='POST':
        fname = request.POST.get('NAME')
        pattern = "^[A-Za-z_-]*$"
        state = bool(re.match(pattern, fname))
        email = request.POST.get('Email')
        lname = request.POST.get('lname')
        message = request.POST.get('Message')
        print(fname, email, lname, message)
        if state == True:
            send = Send(fname=fname, lname=lname, email=email, message=message)
            send.save()
            return HttpResponse("Thanks for contacting")
        if not(state):
            return HttpResponse("Name should be character type")
        else:
            return HttpResponse("enter name")

    return render(request,'et/home.html')
