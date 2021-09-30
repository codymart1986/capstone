from django.shortcuts import render
from .models import Workorder
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def create(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        description = request.POST.get('description')
        hours = request.POST.get('hours')
        body = request.POST.get('body')
            new_order = Workorder(
            user_id=request.user.id,
            name=name,
            description=description,
            hours=hours,
            body=body,
        )
        new_order.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'workorder/create.html')