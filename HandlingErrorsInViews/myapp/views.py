from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Welcome to Siyam lemon")

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("menu for Siyam Lemon")

def book(request):
    return HttpResponse("make a booking")