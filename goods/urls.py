from django.urls import path
from goods.views import index_page

app_name = "goods"

urlpatterns = [
    path('', index_page, name="catalog"),
]