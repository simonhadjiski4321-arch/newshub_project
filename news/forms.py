from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "author_name", "category", "tags"]
        labels = {
            "title": "Заглавие",
            "content": "Съдържание",
            "author_name": "Автор",
            "category": "Категория",
            "tags": "Тагове",
        }
        widgets = {
            "content": forms.Textarea(attrs={"rows": 6}),
        }