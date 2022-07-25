from django.urls import path
from blog_posts import views
from blog_posts.views import delete_entry
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'blog_posts'
urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blogs'),
    path('blog_entry/<int:blog_id>/', views.blog_entry, name='blog_entry'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('add_entry/<int:blog_id>/', views.add_entry, name='add_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name="edit_entry"),
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]