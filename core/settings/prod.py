# core/settings/prod.py


from .base import *
from decouple import config
import os

# برای production همیشه DEBUG=False باشد
DEBUG = False

# اما از env برای سایر تنظیمات استفاده می‌کنیم
ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', default='127.0.0.1,localhost').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME', default='django_db'),
        'USER': config('DATABASE_USER', default='django_user'),
        'PASSWORD': config('DATABASE_PASSWORD', default='django_password'),
        'HOST': config('DATABASE_HOST', default='db'),
        'PORT': config('DATABASE_PORT', default='5432'),
    }
}

# Email Configuration - اضافه کردن تنظیمات ایمیل
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_USE_SSL = config('EMAIL_USE_SSL', default=False, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default=EMAIL_HOST_USER)

# REST Framework Configuration
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": config('PAGE_SIZE', default=3, cast=int),
}

# Security settings for production - اضافه کردن تنظیمات امنیتی
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=True, cast=bool)
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=True, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=True, cast=bool)
SECURE_BROWSER_XSS_FILTER = config('SECURE_BROWSER_XSS_FILTER', default=True, cast=bool)
SECURE_CONTENT_TYPE_NOSNIFF = config('SECURE_CONTENT_TYPE_NOSNIFF', default=True, cast=bool)

# # برای استفاده از static files در production
# STATIC_ROOT = '/app/staticfiles'
# MEDIA_ROOT = '/app/media'