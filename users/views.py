from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def logout_view(request):
    """Log the user out"""
    logout(request)
    #return HttpResponseRedirect(reverse('timer:index'))
    return redirect('timer:index')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)  
        return redirect('timer:index')
    else:
        messages.error(request,'username or password not correct')
        return redirect('timer:index')

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        #Display blank registration form
        form = UserCreationForm()
    else:
        #process completed form
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            #Log the user in and then redirect to home page
            
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            auth_login(request, authenticated_user)
            return HttpResponseRedirect(reverse('timer:index'))
        
    context = {'form': form}
    return render(request, 'users/register.html', context)

