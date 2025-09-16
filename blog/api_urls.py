

# /home/majid/django/django/blog/api_urls.py
from django.urls import path
from . import api_views

app_name = "blog_api"

urlpatterns = [
    path("", api_views.PostListAPI.as_view(), name="post_list_api"),
    path("<int:pk>/", api_views.PostDetailAPI.as_view(), name="post_detail_api"),
]
