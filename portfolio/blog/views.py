from django.shortcuts import render, get_object_or_404

from .models import Blog


def all_blog(request):
    blogs = Blog.objects

    data = {
        'site': 'Blog',
        'blogs': blogs
    }
    return render(request, 'blog/all_blog.html', data)


def detail(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)

    data = {
        'site': 'Blog',
        'post': post
    }

    return render(request, 'blog/detail.html', data)
