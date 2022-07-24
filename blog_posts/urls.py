from django.urls import path
from blog_posts import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'blog_posts'
urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blogs'),
    path('blog_entry/<int:blog_id>/', views.blog_entry, name='blog_entry'),
]