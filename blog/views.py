
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


def post_detail(request, id):
    """
    Show details of a single published post.
    """
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    return render(request, 'blog/post/detail.html', {'post': post})

