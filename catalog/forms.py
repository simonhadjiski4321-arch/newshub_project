from django import forms

from .models import Category, Tag


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
        help_texts = {
            "name": "Въведи уникално име за категорията.",
            "description": "Описанието не е задължително.",
        }
        error_messages = {
            "name": {
                "required": "Моля, въведи име на категорията.",
                "max_length": "Името може да е до 50 символа.",
                "unique": "Категория с това име вече съществува.",
            },
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        help_texts = {
            "name": "Въведи уникално име за тага.",
        }
        error_messages = {
            "name": {
                "required": "Моля, въведи име на тага.",
                "max_length": "Името може да е до 30 символа.",
                "unique": "Таг с това име вече съществува.",
            },
        }