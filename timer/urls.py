from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views


app_name = 'timer'
urlpatterns = [
    path('', views.index, name='index'),
    path('activities/', views.activities, name='activities'),
    path('activities/new_activity/', views.new_activity, name='new_activity'),
    path('activities/edit_activity/<int:activity_id>/', views.edit_activity, name='edit_activity'),
    path('activities/delete_activity/<int:activity_id>/', views.delete_activity, name='delete_activity'),
    path('activities/update_stopwatch/', views.update_stopwatch, name="update_stopwatch"),
    path('activities/activity/<str:activity_title>/', views.activity_detail, name='activity_detail'),

]