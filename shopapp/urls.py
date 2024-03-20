from django.urls import path
from shopapp.views import index_page

app_name = "shopapp"

urlpatterns = [
    path('', index_page, name='home'),
]