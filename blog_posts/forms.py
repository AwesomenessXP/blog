from django import forms
from blog_posts.models import Blog, BlogEntry

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title'] # make an array
        label = {'title': ''} # make a dictionary

class EntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = ['blog_entry_title', 'date_added', 'text']
        label = {'Title': '', 'Date Addded': '', 'Text': ''}