from __future__ import annotations

from rest_framework import serializers  # type: ignore

from .models import BookCategory


class BookCategorySerializer(serializers.HyperlinkedModelSerializer):  # type: ignore
    class Meta:
        model = BookCategory
        fields = ("id", "name", "parent")
