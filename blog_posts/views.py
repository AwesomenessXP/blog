from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog_posts/base.html')

def blog(request, blog_id):
    return render(request, 'blog_posts/')