from __future__ import annotations

from typing import Any

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

    def validate(self, data: Any) -> Any:
        try:
            if data["parent"] is not None and data["parent"].name == data["name"]:
                raise serializers.ValidationError("The category can't be own parent.")
        except KeyError:
            pass
        return data
