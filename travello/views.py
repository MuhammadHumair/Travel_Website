from django.shortcuts import render

from .models import Destination

# Create your views here.

def index(request):
    '''
    This funcion is used to load model data and render the index page.
    '''

    dic = Destination.objects.all()
    
    return render(request, "index.html", {'dests':dic})
