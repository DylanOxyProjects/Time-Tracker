from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from timer.stopwatch import Timer

from timer.models import Activity
from timer.forms import ActivityForm, ActivityFormEdit

def index(request):
    return render(request, 'timer/index.html') 

@login_required   
def activities(request):
    
    activities = Activity.objects.filter(owner=request.user).order_by('-activity_time')[:]
    context = {'activities':activities}
    #the render() function takes the rquest object as its first argument, a template name as its second
    #argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given
    #template rendered with the given context
    return render(request, 'timer/activities.html', context)

@login_required 
def activity_detail(request, activity_id):

    activity = Activity.objects.get(id=activity_id)
    #make sure the topic belonds to the curent user
    if activity.owner != request.user:
        raise Http404
    return render(request, 'timer/activity_detail.html', {'activity': activity})

def activity_start(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    timer = Timer()
    start = timer.start()
    
    return render(request, 'timer/activity_start.html', {'start': start, 'activity': activity})


def activity_stop(request, start, activity_id):
    
    stop = Timer()
    total_time = start - stop
    
    activity = Activity.objects.get(id=activity_id)
    activity.activity_time = activity.activity_time + total_time
    
    return render(request, 'timer/activity_detail.html', {'activity': activity})
    


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
            return HttpResponseRedirect(reverse('timer:activity_detail', args=[activity.id]))
        
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
