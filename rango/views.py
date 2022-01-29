from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, "rango/index.html", context = context_dict)

def about(request):
    context_dict = {'boldmessage': 'here is the about page.', 'signature': "This tutorial has been put together by Dominic Jina"}
    return render(request, "rango/about.html", context=context_dict)
    #return HttpResponse("Rango says here is the about page.")

# Create your views here.
