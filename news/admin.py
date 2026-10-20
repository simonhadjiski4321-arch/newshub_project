from django.contrib import admin

from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author_name", "category", "created_at")
    list_filter = ("category", "tags", "created_at")
    search_fields = ("title", "content", "author_name")
    filter_horizontal = ("tags",)

# Register your models here.
