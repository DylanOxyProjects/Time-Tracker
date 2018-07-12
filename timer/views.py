from django.http import Http404
from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponseRedirect
from django.urls import reverse

from timer.models import Activity
from timer.forms import ActivityForm

def index(request):
    return render(request, 'timer/index.html') 
   
def activities(request):
    
    activities = Activity.objects.order_by('-activity_time')[:]
    context = {'activities':activities}
    #the render() function takes the rquest object as its first argument, a template name as its second
    #argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given
    #template rendered with the given context
    return render(request, 'timer/activities.html', context)

def activity_detail(request, activity_id):
    
    #the get_object_or_404 takes a django model as its first argument and an arbitrary number of keyword arguments, 
    #which it passe sto the get() function of the model's manager. It raises Http404 if the object doesnt exist
    #activity = get_object_or_404(Activity, pk=activity_id)
    activity = Activity.objects.get(id=activity_id)
    
    
    
    return render(request, 'timer/activity_detail.html', {'activity': activity})
    
def new_activity(request):
    """Add a new activity"""
    if request.method != 'POST': 
        #No data submitted, create a blank form
        form = ActivityForm()   
    else:
        #POST data submitted; process data
        form = ActivityForm(request.POST)  
        if form.is_valid():   
            form.save()    
            
            #activity_title = form.cleaned_data['activity_title']
            #activity = Activity.objects.filter(activity_title=activity_title)
            
            return HttpResponseRedirect(reverse('timer:activities'))   
    context = {'form': form}   
    return render(request, 'timer/new_activity.html', context)


def edit_activity(request, activity_id):
    """Edit an existing activity"""
    activity = Activity.objects.get(id=activity_id)
    
    if request.method != 'POST':
        #initial request; pre-fill form with current entry
        form = ActivityForm(instance=activity)
    else:
        # POST data submitted; process data
        form = ActivityForm(instance=activity, data=request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('timer:activity_detail', args=[activity.id]))
        
    context = {'activity': activity, 'form': form}
    return render(request, 'timer/edit_activity.html', context)


def delete_activity(request, activity_id):
    """delete an existing activity"""
    activity = Activity.objects.get(id=activity_id)
    activity.delete()
    return HttpResponseRedirect(reverse('timer:activities')) 
