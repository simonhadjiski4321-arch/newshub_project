from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Име"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание"
    )

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Име"
    )
    def __str__(self):
        return self.name
