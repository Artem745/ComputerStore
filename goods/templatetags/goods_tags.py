from django import template
from django.db.models import Prefetch
from django.utils.http import urlencode

from goods.models import Categories

register = template.Library()


@register.simple_tag()
def tag_categories_with_subcategories():
    return Categories.objects.filter(parent_category=None).prefetch_related(
        Prefetch(
            "sub_categories",
            queryset=Categories.objects.prefetch_related("sub_categories"),
        )
    )


@register.simple_tag()
def tag_certain_subsategories(category_url):
    return Categories.objects.filter(parent_category__slug=category_url)


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context["request"].GET.dict()
    query.update(kwargs)
    return urlencode(query)
