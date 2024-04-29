from django.shortcuts import render
from django.http import HttpResponse

from myapp.forms import InputForm
# Create your views here.

def formview(request):
    form = InputForm()
    context = {"form": form}
    return render(request,"home.html", context)