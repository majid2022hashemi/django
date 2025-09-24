
# api/urls.py

from django.urls import path
from django.http import JsonResponse

app_name = "api"

def api_root(request):
    return JsonResponse({
        "blog_api": "/api/blog/",
        "docs": "/api/docs/"  # می‌تونی بعداً اضافه کنی
    })

urlpatterns = [
    path("", api_root, name="api-root"),
]
