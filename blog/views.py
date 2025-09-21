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
    model = Post
    template_name = 'blog/post/detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'post'  # مطابق با نام kwarg در urls.py

    def get_queryset(self):
        return Post.published.filter(
            publish__year=self.kwargs['year'],
            publish__month=self.kwargs['month'],
            publish__day=self.kwargs['day']
        )


