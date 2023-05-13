from django.shortcuts import render, redirect
# from .forms import registerform
from django.contrib.auth.models import auth
from django.contrib.auth import login as auth_login
from .forms import registerform
from django.contrib.auth import logout as core_logout

"""Register views for the users' app"""
def register(request):
    if request.method != 'POST':
        form = registerform()

    else:
        form = registerform(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            auth.login(request, new_user)
            return redirect('users:login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

"""Logging out views of users app"""
def logged_out(request):
    core_logout(request)
    return redirect('books:index')
