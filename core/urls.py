
from django.contrib import admin
from django.urls import path
from blog.views import home

urlpatterns = [
    path("", home, name="home"),   # صفحه اصلی
    path("admin/", admin.site.urls),
]


