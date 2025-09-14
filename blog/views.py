

# blog/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello Django + Docker + Nginx 👋</h1>")

    