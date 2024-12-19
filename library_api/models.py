from __future__ import annotations

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year_of_birth_date = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        constraints = [models.UniqueConstraint(fields=["first_name", "last_name"], name="unique_full_name")]


class BookCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, related_name="subcategories")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Book categories"


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    category = models.ManyToManyField(BookCategory, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
