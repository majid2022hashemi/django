# from rest_framework import generics
# from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
# from blog.models import Post
# from .serializers import PostSerializer

# class PostListAPI(generics.ListCreateAPIView):
#     queryset = Post.published.all()
#     serializer_class = PostSerializer
#     renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

# class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.published.all()
#     serializer_class = PostSerializer
#     renderer_classes = [BrowsableAPIRenderer, JSONRenderer]


from rest_framework import generics, filters
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from blog.models import Post
from .serializers import PostSerializer


class PostListAPI(generics.ListCreateAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["publish", "title"]
    search_fields = ["title", "body"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
