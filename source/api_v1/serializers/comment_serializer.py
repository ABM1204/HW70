from rest_framework import serializers
from webapp.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'article', 'text', 'likes_count', 'created_at', 'updated_at']