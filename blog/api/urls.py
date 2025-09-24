
# blog/api/urls.py
from django.urls import path
from . import views

app_name = "blog_api"

urlpatterns = [
    path("", views.PostListAPI.as_view(), name="post_list_api"),
    path("<int:pk>/", views.PostDetailAPI.as_view(), name="post_detail_api"),
    path("posts/<int:pk>/share/", views.PostShareAPI.as_view(), name="post_share_api"),
    path('posts/<int:post_id>/comments/', views.CommentListCreateAPI.as_view(), name='comment-list-create'),
]


