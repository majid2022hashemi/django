
# blog/api/urls.py
from django.urls import path
from . import views

app_name = "blog_api"

urlpatterns = [
    # Posts
    path("", views.PostListAPI.as_view(), name="post_list_api"),
    path("<int:pk>/", views.PostDetailAPI.as_view(), name="post_detail_api"),
    path("<int:pk>/share/", views.PostShareAPI.as_view(), name="post_share_api"),

    # Comments (nested under posts)
    path("<int:post_id>/comments/", views.CommentListCreateAPI.as_view(), name="comment_list_create_api"),

    # Comment detail (CRUD: retrieve, update, delete)
    path("comments/<int:pk>/", views.CommentDetailAPI.as_view(), name="comment_detail_api"),
]
