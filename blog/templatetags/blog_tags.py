from ..models import Post, Category
from django import template

register = template.Library()

@register.simple_tag()
def get_recent_post(num=5):
    return list(Post.objects.all())[-1:-num-1:-1]

@register.simple_tag()
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag()
def get_category():
    return Category.objects.all()