from django.shortcuts import render

from .models import Destinations

# Create your views here.

def index(request):
    '''
    This funcion is used to load model data and render the index page.
    '''

    des = Destinations.objects.all()
    dic = {}
    for d_values in des:
        k = 'val' + str(d_values.id)
        dic[k] = {
            'name': d_values.name,
            'desc': d_values.desc,
            'price': d_values.price,
            'image': str(d_values.img)
        }
    context = {'dest':dic}
    return render(request, "index.html", context)
