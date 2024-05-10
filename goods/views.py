from django.db.models import Q, Max, Min
from django.shortcuts import render
from django.http import Http404
from goods.models import Categories, Products
from django.core.paginator import Paginator

from goods.utils import q_search


def index(request, category_slug=None):

    page = request.GET.get("page", 1)
    sort_price = request.GET.get("sort_price", None)
    filter_price_from = request.GET.get("from", None)
    filter_price_to = request.GET.get("to", None)
    limit = request.GET.get("limit", 3)
    query = request.GET.get("q", None)

    if category_slug == "all":
        products = Products.objects.all()
    elif query:
        products = q_search(query)
    else:
        products = Products.objects.filter(
            Q(category__slug=category_slug) | 
            Q(category__parent_category__slug=category_slug) | 
            Q(category__parent_category__parent_category__slug=category_slug)
        )

    if len(products) == 0:
        raise Http404("lox")

    if filter_price_from:
        products = products.filter(price__gte=filter_price_from)
    if filter_price_to:
        products = products.filter(price__lte=filter_price_to)

    if sort_price and sort_price != "default" and len(products) > 1:
        products = products.order_by(sort_price)
        
    price_aggregates = products.aggregate(Max('price'), Min('price'))
    
    paginator = Paginator(products, limit)
    current_page = paginator.page(int(page))

    context = {
        "title": "Comptech - Catalog",
        "products": current_page,
        "category_url": category_slug,
        "quantity": products.count(),
        "max": price_aggregates['price__max'],
        "min": price_aggregates['price__min'],
    }  
    return render(request, "goods/index.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        "title": "Comptech - Product",
        "product": product,
    }
    return render(request, "goods/product.html", context)
