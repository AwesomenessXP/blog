# Blog
I'll be making a blog website to get used to the flow in Django

# Specs:
- Home page
- Blog page
- Add attributes to the blog
- Add edit blog functionality
- Add CRUD (Create Read Update Delete) operations

# What I learned:
- 'many-to-one' relationship in Django is represented by `ForeignKey`
    - `Blog` can be accessed through `Blog Entry`, it's foreign key
    - ex: if `BlogEntry` has a foreign key of `Blog`, then `blog.blogentry_set.all()` is a query of all the blogs entries in blog

- How to debug a page not loading properly:
    - check if the current page has an id
        - make sure it is mapped correctly in urls.py

- access the child's parent class to modify an attribute BEFORE saving it to the database

- ERROR FIXED: when using django-heroku, do:
    - `import django_heroku`
    - `django_heroku.settings(locals())`

# Features I want to add in the future:
- Implementing web sockets
- CI/CD during production
