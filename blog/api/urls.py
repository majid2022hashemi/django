from django.urls import path
from . import views

app_name = "blog_api"

urlpatterns = [
    path("", views.PostListAPI.as_view(), name="post_list_api"),
    path("<int:pk>/", views.PostDetailAPI.as_view(), name="post_detail_api"),
]

