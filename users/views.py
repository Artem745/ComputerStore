from django.shortcuts import render

# Create your views here.
def login_page(request):
    context = {
        "title": "Competh - Log in"
    }
    return render(request, "users/log in.html", context)

def signup_page(request):
    context = {
        "title": "Competh - Sign up"
    }
    return render(request, "users/sign up.html", context)