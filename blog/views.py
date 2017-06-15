from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Tag, Category
from comments.forms import CommentForm
import markdown
from django.db.models.aggregates import Count
# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    context = {
        'post_list' : post_list
    }
    return render(request, 'blog/index.html', context)

def ful_wid_post(request):
    post_list = Post.objects.all().order_by('-created_time')
    context = {
        'post_list' : post_list
    }
    return render(request, 'blog/full-width.html', context)

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                     'markdown.extensions.codehilite',
                                  ])
    post.increase_view()
    url_to_post = str(request.get_raw_uri())
    comment_list=post.comment_set.all()
    form=CommentForm()
    context={
        'post':post,
        'url':url_to_post,
        'form':form,
        'comment_list':comment_list
    }
    return render(request, 'blog/detail.html', context=context)

def archives(request, year, month):
    date = str(year)+'-'+(month if int(month) >= 10 else str(0)+str(month))
    post_list=Post.objects.filter(created_time__startswith=date).order_by('-created_time')
    return render(request, 'blog/index.html', {'post_list':post_list})

def category(request, pk):
    name=get_object_or_404(Category, pk=pk)
    post_list=Post.objects.filter(category=name)
    # post_list=Category.objects.annotate(num_posts=Count('post'))
    return render(request, 'blog/index.html', {'post_list':post_list})

