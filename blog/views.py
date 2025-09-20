
# /home/majid/django/django/blog/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def post_list(request, debug=False):
    """
    List all published posts.
    If debug=True, return a simple HttpResponse for testing.
    """
    try:
        posts = Post.published.all()
        if debug:
            return HttpResponse(f"Found {posts.count()} published posts")
        return render(request, 'blog/post/list.html', {'posts': posts})
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )