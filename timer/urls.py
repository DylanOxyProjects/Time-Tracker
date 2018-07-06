from django.urls import path

from . import views
app_name = 'timer'
urlpatterns = [
    path('', views.index, name='index'),
    path('activities/', views.activities, name='activities'),
    path('activities/<int:activity_id>/', views.activity_detail, name='activity_detail'),

]