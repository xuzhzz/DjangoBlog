from ..models import Post, Category
from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag()
def get_recent_post(num=5):
    return list(Post.objects.all())[:5]

@register.simple_tag()
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag()
def get_category():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)