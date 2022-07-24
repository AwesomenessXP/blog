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

# Features I want to add in the future:
- Implementing web sockets
- CI/CD during development
