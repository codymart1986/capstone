from django.shortcuts import redirect, render


def group_redirect(request):
    """This single view function redirects a user to the customer or employee index if they are in either group"""
    if request.user.groups.filter(name="Customers").exists():
        return redirect('/customers/')
    elif request.user.groups.filter(name="Employees").exists():
        return redirect('/employees/')
    else:
        return render(request, 'home.html')