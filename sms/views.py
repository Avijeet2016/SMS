from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "home.html")


def user_login(request):
    forms = UserLoginForm()
    if request.method == "POST":
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')

    context = {'forms': forms}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')