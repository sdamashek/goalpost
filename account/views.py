from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
#from django.http import HttpResponse as HR
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Your account is disabled.")
        else:
            messages.error(request, "Invalid login.")
    return render(request, 'account/login.html')

def create_account(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        if request.POST['password'] != request.POST['confirmpassword'] or request.POST['password'] == '':
            messages.error(request, "Invalid password or passwords do not match.")
            return render(request, 'account/create.html')
        try:
            user = User.objects.create_user(username, email, request.POST['password'])
        except Exception, e:
            messages.error(request, str(e))
            return render(request, 'account/create.html')
        user = authenticate(username=username, password=request.POST['password'])
        auth_login(request, user)
        messages.success(request, 'Account created and logged in.')
        return redirect('/')
    else:
        return render(request, 'account/create.html')