from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if 'username' in request.session:
        return render(request, "userpanel/index.html")
    else:
        return redirect('/account/login')