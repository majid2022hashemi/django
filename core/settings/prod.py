# core/settings/prod.py


from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME', 'django_db'),
        'USER': os.getenv('DATABASE_USER', 'django_user'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'django_password'),
        'HOST': os.getenv('DATABASE_HOST', 'db'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}


# core/settings/prod.py
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 3,  # مثلا ۳ پست در هر صفحه
}
