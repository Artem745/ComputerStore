from django.urls import path
from users.views import login_page, signup_page

app_name = "auth"

urlpatterns = [
    path('login/', login_page, name="login"),
    path('signup/', signup_page, name="signup")
]