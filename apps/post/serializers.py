from rest_framework import serializers
from apps.Post.models import BoxComment, Post, PostImage


class BoxCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxComment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'

