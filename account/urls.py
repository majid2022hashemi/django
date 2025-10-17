
# account/urls.py

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # آدرس‌های ورود و خروج
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # داشبورد
    path('', views.dashboard, name='dashboard'),
]

