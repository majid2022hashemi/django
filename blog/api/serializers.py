
# blog/api/serializers.py
from rest_framework import serializers
from blog.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'body', 'publish', 'status']

    def validate_title(self, value):
        banned_words = ["تبلیغ", "پورنو", "خرید فوری"]
        for word in banned_words:
            if word.lower() in value.lower():
                raise serializers.ValidationError(f"عنوان نباید شامل '{word}' باشد.")
        return value


class PostShareSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    email = serializers.EmailField()
    to = serializers.EmailField()
    comments = serializers.CharField(required=False, allow_blank=True)




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'name', 'email', 'body', 'created', 'active']
        read_only_fields = ['id', 'created', 'active']
