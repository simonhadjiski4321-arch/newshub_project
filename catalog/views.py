from django.shortcuts import render, redirect
from .forms import CategoryForm, TagForm
from .models import Category, Tag


def category_list(request):
    categories = Category.objects.all().order_by("name")
    return render(
        request,
        "catalog/category_list.html",
        {"categories": categories},
    )


def category_create(request):
    form = CategoryForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("catalog:category_list")

    return render(
        request,
        "catalog/category_form.html",
        {"form": form},
    )


def tag_list(request):
    tags = Tag.objects.all().order_by("name")
    return render(
        request,
        "catalog/tag_list.html",
        {"tags": tags},
    )


def tag_create(request):
    form = TagForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("catalog:tag_list")

    return render(
        request,
        "catalog/tag_form.html",
        {"form": form},
    )

# Create your views here.
