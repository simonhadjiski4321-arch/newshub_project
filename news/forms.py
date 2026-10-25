from django import forms
from django.utils import timezone

from .models import Article


class ArticleForm(forms.ModelForm):
    created_at_display = forms.CharField(
        label="Дата на създаване",
        required=False,
        disabled=True,
    )

    class Meta:
        model = Article
        fields = ["title", "content", "author_name", "category", "tags", "image"]
        labels = {
            "title": "Заглавие",
            "content": "Съдържание",
            "author_name": "Автор",
            "category": "Категория",
            "tags": "Тагове",
            "image": "Снимка към новината",
        }
        help_texts = {
            "title": "Въведи кратко и ясно заглавие.",
            "content": "Напиши съдържанието на новината.",
            "author_name": "Името може да е до 80 символа.",
            "category": "Избери категория за новината.",
            "tags": "Можеш да избереш повече от един таг.",
            "image": "Избери изображение (JPG, PNG или WEBP). Полето не е задължително.",
        }

        error_messages = {
            "title": {
                "required": "Моля, въведи заглавие.",
                "max_length": "Заглавието може да е до 200 символа.",
            },
            "content": {
                "required": "Моля, въведи съдържанието.",
            },
            "author_name": {
                "required": "Моля, въведи името на автора.",
                "max_length": "Името може да е до 80 символа.",
            },
            "category": {
                "required": "Моля, избери категория.",
            },
        }
        widgets = {
            "content": forms.Textarea(attrs={"rows": 6}),
            "image": forms.ClearableFileInput(attrs={"accept": "image/*"}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields["created_at_display"].initial = timezone.localtime(
                self.instance.created_at
            ).strftime("%d.%m.%Y %H:%M")
        else:
            self.fields.pop("created_at_display")