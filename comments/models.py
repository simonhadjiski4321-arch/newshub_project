from django.db import models

class Comment(models.Model):
    article = models.ForeignKey(
        "news.Article",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Новина"
    )
    author_name = models.CharField(
        max_length=80,
        verbose_name="Име"
    )
    content = models.TextField(
        max_length=1000,
        verbose_name="Коментар"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата на създаване"
    )

    def __str__(self):
        return f"Коментар от {self.author_name}"

