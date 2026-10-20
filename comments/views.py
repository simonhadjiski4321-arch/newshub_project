from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from .models import Comment


def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    form = CommentForm(request.POST or None, instance=comment)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("news:article_detail", article_id=comment.article_id)

    return render(
        request,
        "comments/comment_form.html",
        {"form": form, "comment": comment},
    )


def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        article_id = comment.article_id
        comment.delete()
        return redirect("news:article_detail", article_id=article_id)

    return render(
        request,
        "comments/comment_confirm_delete.html",
        {"comment": comment},
    )