from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("categories/", views.category_list, name="category_list"),
    path("categories/create/", views.category_create, name="category_create"),
    path("tags/", views.tag_list, name="tag_list"),
    path("tags/create/", views.tag_create, name="tag_create"),
]