from django.http import Http404
from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponseRedirect
from django.urls import reverse

from timer.models import Activity
from timer.forms import ActivityForm

def index(request):
    return render(request, 'timer/index.html') 
   
def activities(request):
    
    activities = Activity.objects.order_by('activity_time')[:]
    context = {'activities':activities}
    #the render() function takes the rquest object as its first argument, a template name as its second
    #argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given
    #template rendered with the given context
    return render(request, 'timer/activities.html', context)

def activityDetail(request, activity_id):
    
    #the get_object_or_404 takes a django model as its first argument and an arbitrary number of keyword arguments, 
    #which it passe sto the get() function of the model's manager. It raises Http404 if the object doesnt exist
    #activity = get_object_or_404(Activity, pk=activity_id)
    activity = Activity.objects.get(id=activity_id)
    
    return render(request, 'timer/activity_detail.html', {'activity': activity})
    
def new_activity(request):
    """Add a new activity"""
    if request.method != 'POST':  #1
        #No data submitted, create a blank form
        form = ActivityForm()  #2  
    else:
        #POST data submitted; process data
        form = ActivityForm(request.POST)  #3
        if form.is_valid():   #4
            form.save()    #5 
            return HttpResponseRedirect(reverse('timer:activity_detail'))   #6
    context = {'form': form}   #7
    return render(request, 'timer/new_activity.html', context)