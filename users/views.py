from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def login(request):

    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("shopapp:home"))
    else:
        form = UserLoginForm()

    context = {
        "title": "Competh - Log in",
        "form": form,
    }
    return render(request, "users/log in.html", context)

def signup(request):

    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("shopapp:home"))
    else:
        form = UserRegistrationForm()

    context = {
        "title": "Competh - Sign up",
        "form": form,
    }
    return render(request, "users/sign up.html", context)

def profile(request):
    context = {
        "title": "Competh - Profile"
    }
    return render(request, "users/profile.html", context)

def logout(request):
    auth.logout(request)
    return redirect(reverse("shopapp:home"))