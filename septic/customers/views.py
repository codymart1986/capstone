from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Customer
from django.urls import reverse

def index(request):
    user = request.user

    if not Customer.objects.filter(user_id=user.id).exists():
        return redirect('create/')
    else:
        specific_customer = Customer.objects.get(user_id=user.id)
        context = {
            'user': user,
            'specific_customer': specific_customer
        }
        print(user)
        return render(request, 'customers/index.html', context)


def create(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        new_customer = Customer(
            user_id=request.user.id,
            name=name,
            address=address,
            zip_code=zip_code,
        )
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')


def edit(request, option):
    specific_option = option
    user = request.user
    specific_customer = Customer.objects.get(user_id=user.id)
    context = {
        'specific_customer': specific_customer,
        'specific_option': specific_option
    }
    if request.method == 'POST':
        if specific_option == 2:
            specific_customer.name = request.POST.get('name')
            specific_customer.address = request.POST.get('address')
            specific_customer.zip_code = request.POST.get('zip_code')
            specific_customer.save()

        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/edit.html', context)

def emergency(request, option):
    specific_option = option
    user = request.user
    specific_customer = Customer.objects.get(user_id=user.id)
    context = {
        'specific_customer': specific_customer,
        'specific_option': specific_option
    }
    if request.method == 'POST':
        if specific_option == 1:
            specific_customer.name = request.POST.get('name')
            specific_customer.address = request.POST.get('address')
            specific_customer.zip_code = request.POST.get('zip_code')
            specific_customer.emergency = request.POST.get('emergency')
            specific_customer.save() 
