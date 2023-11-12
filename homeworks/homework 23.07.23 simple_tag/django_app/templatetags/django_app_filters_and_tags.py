from ..models import Suggests
from django import template
from django_app import models
from django.template.defaultfilters import floatformat
register =  template.Library()

@register.simple_tag
def format_number(value):

    return floatformat(value, -1)

@register.simple_tag()
def show_latest_posts():
    latest_posts = models.Suggests.objects.filter(status='published')[:3]

    return {"latest_posts":latest_posts}
@register.filter(name="my_slice")
def my_slice(source: str, length: int):
    """"""

    return source[:length]
