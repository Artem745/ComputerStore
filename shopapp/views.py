from django.shortcuts import render

from goods.models import Categories
# Create your views here.

def index_page(request):

    context = {
        'title': "Comptech - Home"
    }
    return render(request, "shopapp/index.html", context)

