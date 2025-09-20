
from rest_framework import serializers
from blog.models import Post

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
