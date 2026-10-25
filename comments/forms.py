from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author_name", "content"]
        labels = {
            "author_name": "Твоето име",
            "content": "Коментар",
        }
        help_texts = {
            "author_name": "Въведи името си.",
            "content": "Коментарът може да е до 1000 символа.",
        }
        error_messages = {
            "author_name": {
                "required": "Моля, въведи името си.",
                "max_length": "Името може да е до 80 символа.",
            },
            "content": {
                "required": "Моля, напиши коментар.",
                "max_length": "Коментарът може да е до 1000 символа.",
            },
        }
        widgets = {
            "author_name": forms.TextInput(
                attrs={"placeholder": "Въведи името си"}
            ),
            "content": forms.Textarea(
                attrs={
                    "placeholder": "Напиши коментар...",
                    "rows": 4,
                }
            ),
        }