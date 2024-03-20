from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request, "users/log in.html")

def signup_page(request):
    return render(request, "users/sign up.html")