
# blog/urls.py

from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),  # لیست پست‌ها
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.PostDetailView.as_view(),
        name='post_detail'
    ),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),

]
