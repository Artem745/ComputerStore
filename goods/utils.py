import os
from django.db.models import Q
from goods.models import Products
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from PIL import Image


def q_search(query):

    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
   
    """1"""
    # vector = SearchVector("name")
    # query = SearchQuery(query)

    # result = (
    #     Products.objects.annotate(rank=SearchRank(vector, query))
    #     .filter(rank__gt=0.01)
    #     .order_by("-rank")
    # )
    # return result

    """2"""
    if len(query) > 1:
        result = Products.objects.filter(name__icontains=query)
        return result
    return Products.objects.none() 
    
    """3"""
    # keywords = [word for word in query.split() if len(word) > 1]

    # q_objects = Q()

    # for token in keywords:
    #     q_objects |= Q(name__icontains=token)

    # return Products.objects.filter(q_objects)


def removebg(old_image_path):
    import requests

    with Image.open(old_image_path) as img:
            format = img.format.lower()
    if format == "webp":
        with Image.open(old_image_path).convert('RGB') as img:
            img.save(old_image_path, 'png') 

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(old_image_path, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'Us6G5czWzZB9tAmidsWSftrU'},
    )
    if response.status_code == requests.codes.ok:
        with open(old_image_path, 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)
