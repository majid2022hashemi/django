
# /home/majid/django/django/core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # مسیر HTML وبلاگ
    path("blog/", include("blog.urls", namespace="blog")),

    # API عمومی پروژه
    path("api/", include("api.urls", namespace="api")),

    # API مربوط به بلاگ
    path("api/blog/", include("blog.api.urls", namespace="blog_api")),
]
