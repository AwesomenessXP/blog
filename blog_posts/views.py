from django.shortcuts import render
from .models import Blog, BlogEntry

# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs':blogs}
    return render(request, 'blog_posts/base.html', context)

def blog(request):
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs':blogs}
    return render(request, 'blog_posts/blog.html', context)

def blog_entry(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    entries = blog.blogentry_set.all() # this uses the 'many to one' relationship
    context = {'blog':blog, 'entries': entries}
    return render(request, 'blog_posts/entry.html', context)