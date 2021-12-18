from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import UserRegisterForm

def logout_view(request):
  logout(request)
  return HttpResponseRedirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return HttpResponseRedirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})
