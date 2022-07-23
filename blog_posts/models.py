from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogEntry(models.Model):
    blog_entry_title = models.CharField(max_length=50)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.blog_entry_title[:50]}"