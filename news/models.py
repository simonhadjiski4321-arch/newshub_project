from django.db import models

class Article(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заглавие"
    )
    content = models.TextField(
        verbose_name="Съдържание"
    )
    author_name = models.CharField(
        max_length=80,
        verbose_name="Автор"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата на създаване"
    )
    category = models.ForeignKey(
        "catalog.Category",
        on_delete=models.PROTECT,
        related_name="articles",
        verbose_name="Категория"
    )
    tags = models.ManyToManyField(
        "catalog.Tag",
        blank=True,
        related_name="articles",
        verbose_name="Тагове"
    )

    def __str__(self):
        return self.title

