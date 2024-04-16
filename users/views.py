from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.forms import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):

    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = auth.authenticate(email=email, password=password)
            if user:
                auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")
                if request.POST.get("next", None):
                    return HttpResponseRedirect(request.POST.get("next"))
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
            auth.login(
                request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
            return HttpResponseRedirect(reverse("shopapp:home"))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()

    context = {
        "title": "Competh - Sign up",
        "form": form,
    }
    return render(request, "users/sign up.html", context)


@login_required
def profile(request):

    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance=request.user)

    context = {"title": "Competh - Profile", "form": form}
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse("user:login"))
