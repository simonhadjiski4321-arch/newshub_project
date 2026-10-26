from django.shortcuts import get_object_or_404, redirect, render

from comments.forms import CommentForm
from .models import Article

from .forms import ArticleForm

from catalog.models import Category, Tag

from django.db.models import Q

from comments.models import Comment

from django.core.paginator import Paginator


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
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    paginator = Paginator(articles, 5)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(
        request,
        "news/article_list.html",
        {
            "articles": page_obj,
            "page_obj": page_obj,
            "categories": categories,
            "tags": tags,
            "query": query,
            "current_category": category_id,
            "current_tag": tag_id,
        },
    )

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    form = CommentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        comment = form.save(commit=False)
        comment.article = article

        parent_comment_id = request.POST.get("parent_comment_id")
        if parent_comment_id:
            comment.parent_comment = get_object_or_404(
                Comment,
                id=parent_comment_id,
                article=article,
            )

        comment.save()
        return redirect(request.path)

    comments = (
        article.comments
        .filter(parent_comment__isnull=True)
        .prefetch_related("replies")
    )

    return render(
        request,
        "news/article_detail.html",
        {
            "article": article,
            "form": form,
            "comments": comments,
        },
    )

def article_create(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        article = form.save()
        return redirect("news:article_detail", article_id=article.id)

    return render(
        request,
        "news/article_form.html",
        {
            "form": form,
            "form_title": "Добави новина",
            "button_text": "Запази новината",
        },
    )

def article_update(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

    if request.method == "POST" and form.is_valid():
        article = form.save()
        return redirect("news:article_detail", article_id=article.id)

    return render(
        request,
        "news/article_form.html",
        {
            "form": form,
            "form_title": "Редактирай новина",
            "button_text": "Запази промените",
        },
    )


def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        article.delete()
        return redirect("news:article_list")

    return render(
        request,
        "news/article_confirm_delete.html",
        {"article": article},
    )

def article_latest(request):
    articles = Article.objects.order_by("-created_at")[:3]
    return render(request, "news/article_latest.html", {"articles": articles})