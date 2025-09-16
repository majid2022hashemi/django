

# /home/majid/django/django/core/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
        'accounts/login/', auth_views.LoginView.as_view(), name='login'
        ),
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
        ),
    path("admin/", admin.site.urls),

    # HTML
    path("blog/", include("blog.urls", namespace="blog")),

    # API
    path("api/blog/", include("blog.api_urls", namespace="blog_api")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)