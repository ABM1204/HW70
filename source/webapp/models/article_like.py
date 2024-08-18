from django.contrib.auth.models import User
from django.db import models
from webapp.models import Article


class ArticleLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        unique_together = ('user', 'article')