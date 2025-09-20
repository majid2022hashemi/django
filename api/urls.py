
# api/urls.py

from django.urls import path

# اگر بعداً view در api/views.py ساختی، می‌تونی import کنی:
# from . import views

app_name = "api"

urlpatterns = [
    # نمونه مسیر پایه، بعداً می‌تونی route های واقعی اضافه کنی
    # path("something/", views.SomeView.as_view(), name="something"),
]
