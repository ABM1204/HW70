from django.contrib.auth.models import User
from django.db import models
from webapp.models import Comment


class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        unique_together = ('user', 'comment')