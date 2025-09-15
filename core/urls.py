

# /home/majid/django/django/core/urls.py


""" 
from django.contrib import admin
from django.urls import path
from blog.views import home

urlpatterns = [
    path("", home, name="home"),   # صفحه اصلی
    path("admin/", admin.site.urls),
]

 """



from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
]
