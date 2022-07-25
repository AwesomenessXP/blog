from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Blog, BlogEntry
from .forms import BlogForm, EntryForm
from django.urls import reverse

# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('date_added') # this is similar to Blog.objects.all() --> blogs = ['Blog 1', 'Blog 2']
    context = {'blogs':blogs} # dictionary 
    return render(request, 'blog_posts/base.html', context)

def blog(request):
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs':blogs}
    return render(request, 'blog_posts/blog.html', context)

def blog_entry(request, blog_id):
    blog = Blog.objects.get(id=blog_id) # get the specific blog id
    entries = blog.blogentry_set.all() # this uses the 'many to one' relationship -> accessed through specific blog
    context = {'blog':blog, 'entries': entries}
    return render(request, 'blog_posts/entry.html', context)

def add_blog(request):
    # logic for 'POST' and 'GET' requests
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)

        # if form is valid, redirect to blog.html
        if form.is_valid():
            form.save()
            return redirect('blog_posts:blogs')

    # if blank or invalid -> go back to add_blog.html
    context = {'form': form}
    return render(request, 'blog_posts/add_blog.html', context)

def add_entry(request, blog_id):
    blog = Blog.objects.get(id=blog_id) # get parent 
    # logic for 'POST' and 'GET' requests
    if request.method != 'POST': # when the form is empty (when the user first visits the page)
        form = EntryForm()
    else: # when the form is full (the user submitted data)
        form = EntryForm(data=request.POST)

        if form.is_valid():
            entry = form.save(commit = False) # dont save it yet! we need to attach this form to the parent
            entry.blog = blog # make sure we add data from its parent
            entry.save() # save to database
            return redirect("blog_posts:blog_entry", blog_id=blog.id)

    context = {'form': form, 'blog': blog}
    return render(request, 'blog_posts/add_entry.html', context)

def edit_entry(request, entry_id):
    entry = BlogEntry.objects.get(id=entry_id)
    blog = entry.blog

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('blog_posts:blog_entry', blog_id=blog.id)

    context = {
        'entry':entry,
        'blog':blog,
        'form':form
    }
    return render(request, 'blog_posts/edit_entry.html', context)

def delete_entry(request, entry_id):
    entry = BlogEntry.objects.get(id=entry_id)
    blog = entry.blog
    entry.delete()
    return HttpResponseRedirect('blog_posts:blog_entry', blog_id=blog.id)
