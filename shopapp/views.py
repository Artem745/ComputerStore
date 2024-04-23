from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse


def index(request):

    context = {
        'title': "Comptech - Home"
    }
    return render(request, "shopapp/index.html", context)

def change_theme(request):
    theme = request.POST.get('theme')
    request.session['theme'] = theme
    return JsonResponse({'status': 'success'})