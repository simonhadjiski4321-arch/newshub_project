from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path("<int:comment_id>/edit/", views.comment_update, name="comment_update"),
    path("<int:comment_id>/delete/", views.comment_delete, name="comment_delete"),
]