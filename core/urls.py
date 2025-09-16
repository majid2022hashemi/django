

# /home/majid/django/django/core/urls.py


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # HTML
    path("blog/", include("blog.urls", namespace="blog")),

    # API
    path("api/blog/", include("blog.api_urls", namespace="blog_api")),
]
