from django.db.models import Q
from goods.models import Products
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


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
