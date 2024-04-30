from django.shortcuts import render
#from django.http import HttpResponse

from myapp.forms import BookingForm
# Create your views here.

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request,"home.html", context)