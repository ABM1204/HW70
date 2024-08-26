from django.urls import path
from api_v1.views.article_views import ArticleView
from api_v1.views.comment_views import CommentView

urlpatterns = [
    path('articles/<int:pk>/', ArticleView.as_view(), name='articles_api'),
    path('articles/<int:article_id>/comments/', CommentView.as_view(), name='comments_list_api'),
    path('comment/<int:pk>/', CommentView.as_view(), name='comments_api'),
]

