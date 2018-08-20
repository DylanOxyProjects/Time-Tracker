"""Defines URL patterns for users"""

from django.conf.urls import url
from django.contrib.auth.views import login
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    #login page
    #path('login/', {'template_name': 'users/login.html'}, name='login'),
    #url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register')
]