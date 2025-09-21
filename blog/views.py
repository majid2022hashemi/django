# /home/majid/django/django/blog/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def post_list(request, debug=False):
    """
    List all published posts with pagination.
    If debug=True, return a simple HttpResponse for testing.
    """
    try:
        post_list = Post.published.all()
        paginator = Paginator(post_list, 3)  # ۳ پست در هر صفحه
         # گرفتن شماره صفحه از آدرس (GET parameter)
        page_number = request.GET.get('page', 1)
        try:
            # گرفتن پست‌های مربوط به اون صفحه
            posts = paginator.page(page_number)
        except PageNotAnInteger:
            # اگر شماره صفحه درست نباشه → صفحه اول
            posts = paginator.page(1)
        except EmptyPage:
            # اگر صفحه‌ای که درخواست شده بزرگتر از تعداد صفحات باشه → آخرین صفحه
            posts = paginator.page(paginator.num_pages)

        if debug:
            return HttpResponse(
                f"Total posts: {paginator.count}, "
                f"Total pages: {paginator.num_pages}, "
                f"Current page: {posts.number}"
            )

        return render(
            request,
            'blog/post/list.html',
            {'posts': posts}
        )
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
