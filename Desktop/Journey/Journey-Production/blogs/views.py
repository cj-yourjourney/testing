from django.shortcuts import render
from .models import Blog
# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all()

    context = {
        "blogs" : blogs
    }

    return render(request,'blogs/blog_list.html', context)


def blog_detail(request, slug):

    blog = Blog.objects.get(slug=slug)

    print(blog.title)

    context = {
        'blog' : blog
    }

    return render(request,'blogs/blog_detail.html', context)
