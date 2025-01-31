from rest_framework import serializers
from webapp.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'status', 'likes_count', 'created_at', 'updated_at']
