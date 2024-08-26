from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response

from api_v1.serializers.comment_serializer import CommentSerializer
from webapp.models import Comment


class CommentView(APIView):

    def get(self, request, pk=None, article_id=None):
        if pk:
            comments = get_object_or_404(Comment, pk=pk)
            serializer = CommentSerializer(comments)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif article_id:
            comments = Comment.objects.filter(article_id=article_id)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


    def post(self, request, article_id):
        data = request.data
        data['article'] = article_id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)