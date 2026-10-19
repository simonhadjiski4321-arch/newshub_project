from django.shortcuts import get_object_or_404, redirect, render

from comments.forms import CommentForm
from .models import Article

from .forms import ArticleForm

from catalog.models import Category, Tag

from django.db.models import Q


def article_list(request):
    articles = Article.objects.all().order_by("-created_at")
    categories = Category.objects.all()
    tags = Tag.objects.all()

    category_id = request.GET.get("category")
    tag_id = request.GET.get("tag")
    query = request.GET.get("q", "").strip()

    if category_id:
        articles = articles.filter(category_id=category_id)

    if tag_id:
        articles = articles.filter(tags__id=tag_id)

    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    return render(
        request,
        "news/article_list.html",
        {
            "articles": articles,
            "categories": categories,
            "tags": tags,
            "query": query,
        },
    )

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    form = CommentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect(request.path)

    return render(
        request,
        "news/article_detail.html",
        {
            "article": article,
            "form": form,
        },
    )

def article_create(request):
    form = ArticleForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        article = form.save()
        return redirect("news:article_detail", article_id=article.id)

    return render(
        request,
        "news/article_form.html",
        {"form": form},
    )
