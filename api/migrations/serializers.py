from rest_framework import serializers
from api.models import Post
from api import models

class PostListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)

    def create(self, validated_data):
        post_list = Post(**validated_data)
        post_list.save()
        return post_list

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.name)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    task_list = PostListSerializer(required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.like_count = validated_data.get('like_count', instance.like_count)
        instance.save()
        return instance