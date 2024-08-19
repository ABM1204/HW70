from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import CommentForm
from webapp.models import Article, Comment
from webapp.models.comment_like import CommentLike


class CreateCommentView(LoginRequiredMixin, CreateView):
    template_name = "comments/create_comment.html"
    form_class = CommentForm

    # def form_valid(self, form):
    #     article = get_object_or_404(Article, pk=self.kwargs['pk'])
    #     form.instance.article = article
    #     return super().form_valid(form)

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs['pk'])
        comment = form.save(commit=False)
        comment.article = article
        comment.author = self.request.user
        comment.save()
        return redirect(article.get_absolute_url())

    # def get_success_url(self):
    #     return reverse("webapp:article_detail", kwargs={"pk": self.object.article.pk})


class UpdateCommentView(UpdateView):
    template_name = "comments/update_comment.html"
    form_class = CommentForm
    model = Comment

    def get_success_url(self):
        return reverse("webapp:article_detail", kwargs={"pk": self.object.article.pk})


class DeleteCommentView(DeleteView):
    queryset = Comment.objects.all()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect("webapp:article_detail", pk=self.object.article.pk)


def comment_like(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    user = request.user

    if request.method == "POST":
        like, created = CommentLike.objects.get_or_create(user=user, comment=comment)
        if created:
            comment.likes_count += 1
            comment.save()
    elif request.method == "DELETE":
        like = CommentLike.objects.filter(user=user, comment=comment).first()
        if like:
            like.delete()
            comment.likes_count -= 1
            comment.save()

    return JsonResponse({"likes_count": comment.likes_count})
