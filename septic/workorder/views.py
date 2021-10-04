from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from .models import Workorder
from django.urls import reverse



def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        hours = request.POST.get('hours')
        description = request.POST.get('description')
        body = request.POST.get('body')
        recommendations = request.POST.get('recommendations')
        new_order = Workorder(name=name, hours=hours, description=description, body=body, recommendations=recommendations)
        new_order.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'create.html')
