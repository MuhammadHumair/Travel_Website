from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method== 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password1']
        cpwd = request.POST['password2']
        
        if User.objects.filter(username=uname):
            messages.info(request, "Username already registered ...!!!")
            return redirect('register')
        elif User.objects.filter(email=email):
            messages.info(request, "Email already registered ...!!!")
            return redirect('register')
        elif pwd != cpwd:
            messages.info(request, "Password and Confirm Password are not matched ...!!!")
            return redirect('register')
        else:
            data = User.objects.create_user(first_name=fname, last_name=lname, username=uname, password=pwd, email=email)
            data.save()
            #messages.success(request, "You are successfully registered ...!!!")
            return redirect('login')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']

        data = auth.authenticate(username=uname, password=pwd)

        if data is not None:
            auth.login(request, data)
            #messages.success(request, "Login Successfully...!!!")
            return redirect('/')
        else:
            messages.info(request, "Login and Password not matched...!!!")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")