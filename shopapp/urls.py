from django.urls import path
from shopapp.views import index, change_theme

app_name = "shopapp"

urlpatterns = [
    path('', index, name='home'),  
    path('change-theme/', change_theme, name='change_theme'), 
]