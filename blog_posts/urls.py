from django.urls import path
from blog_posts import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'blog_posts'
urlpatterns = [
    path('', views.test, name='home')
]