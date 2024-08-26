from django.urls import path
from api_v1.views.article_views import ArticleView

urlpatterns = [
    path('articles/<int:pk>/', ArticleView.as_view(), name='articles_api'),
]

