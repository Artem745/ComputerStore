from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import Http404, HttpResponse
from goods.models import Products, Categories
from django.core.paginator import Paginator

from goods.utils import q_search


def index_page(request, category_slug=None):
    
    page = request.GET.get('page', 1)
    sort_price = request.GET.get('sort_price', None)
    limit = request.GET.get('limit', 3)
    query = request.GET.get('q', None)

    # products = Products.objects.all()

    # if sort_price and sort_price != "default" and len(products) > 1:
    #     products = products.order_by(sort_price)

    # if category_slug != "all":
    #     products = get_list_or_404(products.filter(category__slug=category_slug))

    if category_slug == "all":
        products = Products.objects.all()
    elif query:
        products = q_search(query)
    else:
        products = Products.objects.filter(category__slug=category_slug)
    
    if len(products) == 0:
        raise Http404("lox")

    if sort_price and sort_price != "default" and len(products) > 1:
        products = products.order_by(sort_price)

    # if category_slug == "all":
    #     products = Products.objects.all()
    # else:
    #     products = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    # if sort_price and sort_price != "default" and len(products) > 1:
    #     products = products.order_by(sort_price)
    
    paginator = Paginator(products, limit)
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
