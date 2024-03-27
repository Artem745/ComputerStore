from django.shortcuts import render

from goods.models import Products, Categories


def index_page(request):
    
    goods = Products.objects.all()

    context = {
        "title": "Comptech - Catalog",
        "goods": goods,
    }
    return render(request, "goods/index.html", context)
