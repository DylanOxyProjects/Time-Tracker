from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse 
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from timer.models import Activity
from timer.forms import ActivityForm, ActivityFormEdit

from datetime import timedelta
import json

def index(request):
    return render(request, 'timer/index.html') 

@login_required   
def activities(request):
    
    activities = Activity.objects.filter(owner=request.user).order_by('-activity_time')[:]
    context = {'activities':activities}
    return render(request, 'timer/activities.html', context)

@login_required
def activity_detail(request, activity_title):
    activity = Activity.objects.get(activity_title=activity_title)
    if activity.owner != request.user:
        raise Http404
    
    if (len(activity.activity_time) != 14):
        activity.activity_time = "0000:00:00.000"
        
    context = {'activity':activity}
    return render(request, 'timer/activity_detail.html', context)


@login_required
def update_stopwatch(request):
    """
    incorporates ajax. every 4-5 seconds sends updates
    on new activity_time to be stored while the user
    is using the stopwatch in activity_detail
    """
    updateString = request.body.decode("utf-8")
    updateStringList = updateString.split('$$TEXT$$')
    time = updateStringList[0]
    activity = Activity.objects.get(activity_title=updateStringList[1])
    
    if activity.owner != request.user:
        raise Http404  
    
    activity.activity_time = time
    activity.save()
    return HttpResponse("")
    
    
    
@login_required 
def new_activity(request):
    """Add a new activity"""
    if request.method != 'POST': 
        #No data submitted, create a blank form
        form = ActivityForm()   
    else:
        #POST data submitted; process data
        form = ActivityForm(request.POST)  
        if form.is_valid():   
            new_activity = form.save(commit=False)
            new_activity.owner = request.user
            new_activity.save()
            
            
            #activity_title = form.cleaned_data['activity_title']
            #activity = Activity.objects.filter(activity_title=activity_title)
            
            return HttpResponseRedirect(reverse('timer:activities'))   
    context = {'form': form}   
    return render(request, 'timer/new_activity.html', context)

@login_required 
def edit_activity(request, activity_id):
    """Edit an existing activity"""
    activity = Activity.objects.get(id=activity_id)
    if activity.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        #initial request; pre-fill form with current entry
        form = ActivityFormEdit(instance=activity)
    else:
        # POST data submitted; process data
        form = ActivityFormEdit(instance=activity, data=request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('timer:activities'))
        
    context = {'activity': activity, 'form': form}
    return render(request, 'timer/edit_activity.html', context)

@login_required 
def delete_activity(request, activity_id):
    """delete an existing activity"""
    activity = Activity.objects.get(id=activity_id)
    if activity.owner != request.user:
        raise Http404    
    activity.delete()
    return HttpResponseRedirect(reverse('timer:activities')) 
