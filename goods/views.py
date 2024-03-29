from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Products, Categories


def index_page(request):
    
    products = Products.objects.all()

    context = {
        "title": "Comptech - Catalog",
        "products": products,
    }
    return render(request, "goods/index.html", context)

def product_page(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        "title": "Comptech - Catalog",
        "product": product,
    }
    return render(request, "goods/product.html", context)