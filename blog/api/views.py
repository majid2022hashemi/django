
# blog/api/views.py

from rest_framework import generics, filters, status
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from blog.models import Post
from .serializers import PostSerializer, PostShareSerializer
from rest_framework.response import Response
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

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


class PostShareAPI(generics.GenericAPIView):
    serializer_class = PostShareSerializer

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=Post.Status.PUBLISHED)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            cd = serializer.validated_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} ({cd['email']}) recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['name']}'s comments: {cd['comments']}"

            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cd['to']]
            )
            return Response({"success": True, "message": "Email sent successfully!"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
