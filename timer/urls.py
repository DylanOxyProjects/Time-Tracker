from django.urls import path

#In order to understand what regular expressions are and what they do,
#
#\d any number
#\D anything but a number 
#\s space
#\S anything but a space 
#\w any character
#\W anything but a character
#. = any character except a new line
#\b the whitespce around words 
#\. a period 
#MODIFIERS:
#
#{1,3} we're expecting 1-3
#+ match one or more 
#? match 0 or 1 
#* match 0 or more 
#$ match the end of a string 
#^ match the begining of a string 
#| either or 
#[] a range or "variance" [1-5a-qA-Z]
#{x} expecting "x" amount 
#
#white space characters \n new line 
#\s space
#\t tab
#\e escape 
#\f form feed
#\r return 

#DONT FORGET!

#. + * ?  [] $  ^  ()  {}  | \ 
#https://docs.python.org/3.4/library/re.html

from . import views
app_name = 'timer'
urlpatterns = [
    path('', views.index, name='index'),
    path('activities/', views.activities, name='activities'),
    path('activities/<int:activity_id>/', views.activity_detail, name='activity_detail'),
    #path(r'^activity_detail/(?P<activity_id>\d+)/$', views.activity_detail, name='activity_detail'),
    path('activities/new_activity/', views.new_activity, name='new_activity'),
    path('activities/edit_activity/<int:activity_id>/', views.edit_activity, name='edit_activity') 
    

]