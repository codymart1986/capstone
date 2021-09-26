from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Employees
from django.apps import apps


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employees(
            user_id=request.user.id,
            name=name,
            zip_code=zip_code
        )
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')

def index(request):
    user = request.user
    if not Employees.objects.filter(user_id=user.id).exists():
        return redirect('create/')
    else:
        specific_employee = Employees.objects.get(user_id=user.id)
        specific_employee.save()
        context = {
            'user': user,
            'specific_employee': specific_employee
        }
        return render(request, 'employees/index.html', context)
