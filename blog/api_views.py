# blog/api_views.py
from rest_framework import generics
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import Post
from .serializers import PostSerializer

class PostListAPI(generics.ListCreateAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]  # اضافه شد

class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]  # اضافه شد
