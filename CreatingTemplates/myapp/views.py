from django.shortcuts import render
#from myapp.forms import BookingForm

def about(request):
    about_content = {'about': 'We eat with our eyes first, but before we see our food, we picture it while reading the menu descriptions. They say one image is worth a thousand words, but don’t underestimate the power of words. A few strategically placed words here and there can make your food and wine descriptions increase your restaurant’s sales'}
    return render(request, "about.html", about_content)



#def form_view(request):
 #   form = BookingForm()
  #  if request.method == 'POST':
   #     form = BookingForm(request.POST)
    ##       form.save()
    #context = {"form" : form}
    #return render(request, "booking.html", context)