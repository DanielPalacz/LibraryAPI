from __future__ import annotations

from rest_framework import serializers  # type: ignore

from .models import BookCategory


class BookCategorySerializer(serializers.HyperlinkedModelSerializer):  # type: ignore
    class Meta:
        model = BookCategory
        fields = ("id", "name", "parent")

    @staticmethod
    def validate_name(value: str) -> str:
        if len(value) < 3:
            raise serializers.ValidationError("Category name should have at least 3 letters.")
        return value
