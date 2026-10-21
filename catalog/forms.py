from django import forms
from .models import Category, Tag


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]