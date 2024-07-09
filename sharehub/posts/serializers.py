from typing import Any, Dict

from rest_framework import serializers
from rest_framework.request import Request

from .models import LikePost, Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    caption = serializers.CharField(required=False, allow_blank=True)
    img = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'caption', 'img', 'date_posted', 'date_updated']
        read_only_fields = ['id', 'author', 'date_posted', 'date_updated']
    
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        if not attrs.get('caption') and not attrs.get('img'):
            raise serializers.ValidationError("Either caption or img is required.")
        return attrs
    
    def create(self, validated_data: Dict[str, Any]) -> Post:
        request: Request = self.context.get('request')
        post = Post.objects.create(author=request.user, **validated_data)
        return post


class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = ['id', 'user', 'post', 'value']
        read_only_fields = ['id', 'user', 'post']

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        if not attrs.get('value'):
            raise serializers.ValidationError("Value is required.")
        return attrs
    
    def create(self, validated_data: Dict[str, Any]) -> LikePost:
        request: Request = self.context.get('request')
        like_post = LikePost.objects.create(user=request.user, **validated_data)
        return like_post
