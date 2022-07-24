from django.contrib import admin
from blog_posts.models import Blog, BlogEntry

# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogEntry)