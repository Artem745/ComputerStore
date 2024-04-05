from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        "title": "Competh - Log in"
    }
    return render(request, "users/log in.html", context)

def signup(request):
    context = {
        "title": "Competh - Sign up"
    }
    return render(request, "users/sign up.html", context)

def profile(request):
    context = {
        "title": "Competh - Profile"
    }
    return render(request, "users/log in.html", context)

def logout(request):
    ...