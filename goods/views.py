from django.shortcuts import get_list_or_404, render
from django.http import HttpResponse
from goods.models import Products, Categories
from django.core.paginator import Paginator


def index_page(request, category_slug):
    
    page = request.GET.get('page', 1)
    sort_price = request.GET.get('sort_price', None)

    if category_slug == "all":
        products = Products.objects.all()

    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if sort_price and sort_price != "default":
        products = products.order_by(sort_price)

    paginator = Paginator(products, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Comptech - Catalog",
        "products": current_page,
        "category_url": category_slug,
    }
    return render(request, "goods/index.html", context)


def product_page(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        "title": "Comptech - Product",
        "product": product,
    }
    return render(request, "goods/product.html", context)
