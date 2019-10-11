from django.shortcuts import render, redirect
from .forms import EmployeeForm
from django.contrib.auth.models import User

def create_employee(request):
    forms = EmployeeForm()
    if request.method == "POST":
        forms = EmployeeForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]
            #print(username, password)
            user_obj = User.objects.create_user(username=username, password=password)
            new_user = forms.save(commit=False)
            new_user.user = user_obj
            new_user.save()
            return redirect('home')

    context = {'forms': forms}
    return render(request, 'administration/create_employee.html', context)

    