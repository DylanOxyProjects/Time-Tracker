from random import randint
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from timer.models import Activity
from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse

def index(request):
    url = reverse('timer:activities')
    return render(request, 'timer/index.html')


def activities(request):

    activities = Activity.objects.order_by('activity_time')[:]
    context = {'activities':activities}
    #the render() function takes the rquest object as its first argument, a template name as its second
    #argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given
    #template rendered with the given context
    return render(request, 'timer/activities.html', context)

def activity_detail(request, activity_id):
    #the get_object_or_404 takes a django model as its first argument and an arbitrary number of keyword arguments,
    #which it passe sto the get() function of the model's manager. It raises Http404 if the object doesnt exist
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'timer/activity_detail.html', {'activity': activity})

@csrf_exempt
def formtest(request):

    for key in sorted(request.GET):
        print(f"request.GET[{key}] = {request.GET[key]}")
    for key in sorted(request.POST):
        print(f"request.POST[{key}] = {request.POST[key]}")
    for key in sorted(request.COOKIES):
        print(f"request.COOKIES[{key}] = {request.COOKIES[key]}")

    if request.method == 'POST':
        if 'formtoken' not in request.POST or request.POST['formtoken'] != request.COOKIES['formtoken']:
            return HttpResponse(b'FAIL!!!\n')

    # create a "formtoken" and put in the form as a hidden input and as a cookie value
    form_token = randint(100000, 999999)
    context = {'formtoken': form_token}

    response = render(request, 'timer/formtest.html', context)
    response.set_cookie('formtoken', form_token)
    return response
