from django.urls import path
from goods.views import index, product

app_name = "goods"

urlpatterns = [
    path('search/', index, name="search"),
    path('<slug:category_slug>/', index, name="index"),
    path('product/<slug:product_slug>/', product, name="product"),
    
]