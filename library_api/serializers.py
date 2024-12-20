from __future__ import annotations

from typing import Any

from rest_framework import serializers  # type: ignore

from .models import Author
from .models import Book
from .models import BookCategory


class AuthorSerializer(serializers.HyperlinkedModelSerializer):  # type: ignore
    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "year_of_birth_date")

    @staticmethod
    def validate_first_name(value: str) -> str:
        if len(value) < 2:
            raise serializers.ValidationError("First name should have at least 2 letters.")
        return value

    @staticmethod
    def validate_last_name(value: str) -> str:
        if len(value) < 2 or value == "-":
            raise serializers.ValidationError("Last name should have at least 2 letters.")
        return value


class BookSerializer(serializers.HyperlinkedModelSerializer):  # type: ignore
    class Meta:
        model = Book
        fields = ("id", "title", "author", "category")


class BookCategorySerializer(serializers.HyperlinkedModelSerializer):  # type: ignore
    class Meta:
        model = BookCategory
        fields = ("id", "name", "parent")

    @staticmethod
    def validate_name(value: str) -> str:
        if len(value) < 3:
            raise serializers.ValidationError("Category name should have at least 3 letters.")
        return value

    def validate(self, data: Any) -> Any:
        try:
            if data["parent"] is not None and data["parent"].name == data["name"]:
                raise serializers.ValidationError("The category can't be own parent.")
        except KeyError:
            pass
        return data
