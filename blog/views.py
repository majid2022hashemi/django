# blog/views.py

from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    """
    Class-Based View for listing published posts with pagination
    """
    queryset = Post.published.all()        # پست‌های منتشر شده
    context_object_name = 'posts'          # اسم متغیر در template
    paginate_by = 3                         # ۳ پست در هر صفحه
    template_name = 'blog/post/list.html'  # قالب دلخواه



class PostDetailView(DetailView):
    """
    Class-Based View for a single published post
    """
    model = Post
    template_name = 'blog/post/detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        """
        Limit queryset to published posts only
        """
        return Post.published.all()
