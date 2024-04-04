from django.urls import path
from goods.views import index_page, product_page

app_name = "goods"

urlpatterns = [
    path('search/', index_page, name="search"),
    path('<slug:category_slug>/', index_page, name="index"),
    path('product/<slug:product_slug>/', product_page, name="product"),
]