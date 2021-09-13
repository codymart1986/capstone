from django import forms
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    is_employee = forms.BooleanField(label="Check to register as employee", required=False)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "is_employee")

    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        user.is_employee = self.cleaned_data["is_employee"]

        
        if commit:
            user.save()
            if user.is_employee:
                employees = Group.objects.get(name="Employees")
                employees.user_set.add(user)
            else:
                customers = Group.objects.get(name="Customers")
                customers.user_set.add(user)
        return user
