"""time_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


app_name = 'timer'
urlpatterns = [
    #the include function allows referencing other URLconfs.
    #django chops off whatever part of teh URL up to that point and sends the 
    #remaining string to the included URLconf for further processing.
    path('timer/', include('timer.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),   
]
