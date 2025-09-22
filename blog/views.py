# blog/views.py

from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import EmailPostForm
from django.shortcuts import get_object_or_404, render

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


def post_share(request, post_id):
    # 1. Retrieve post by id
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )
    sent = False

    # 2. Check if the request is GET or POST
    if request.method == 'POST':
        # The form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # If the form is valid → process the data
            cd = form.cleaned_data
            # (Here we will send the email later)
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = (
                f"{cd['name']} ({cd['email']}) "
                f"recommends you read {post.title}"
            )
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}'s comments: {cd['comments']}"
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cd['to']],
            )
            sent = True

    else:
        # If it's a GET request → create an empty form
        form = EmailPostForm()

    # 3. Render the page with the form
    return render(
        request,
        'blog/post/share.html',
        {
            'post': post,
            'form': form,
            'sent': sent
        },
    )
