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