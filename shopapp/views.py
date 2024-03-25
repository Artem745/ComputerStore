from django.shortcuts import render

from goods.models import Categories
# Create your views here.

def index_page(request):
    categories = Categories.objects.all()

    context = {
        'categories': categories
    }
    return render(request, "shopapp/index.html", context)

