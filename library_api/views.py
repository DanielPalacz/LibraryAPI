from __future__ import annotations

from typing import Type

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import serializers  # type: ignore
from rest_framework import viewsets
from rest_framework.generics import ListAPIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework.views import APIView  # type: ignore

from .models import Author
from .models import Book
from .models import BookCategory
from .serializers import AuthorSerializer
from .serializers import BookCategorySerializer
from .serializers import BookSerializer

# from django.shortcuts import render


@extend_schema(
    tags=["Authors"],
)
class AuthorViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Author.objects.all().order_by("last_name")
    serializer_class = AuthorSerializer


@extend_schema(
    tags=["Autor books"],
    responses=BookSerializer(many=True),
)
class AuthorBooksView(ListAPIView):  # type: ignore
    """The given Author books."""

    serializer_class = BookSerializer

    def get_queryset(self) -> QuerySet:  # type: ignore
        user_id = self.kwargs["pk"]
        author = get_object_or_404(Author, pk=user_id)
        return author.books.all()


@extend_schema(
    tags=["Books"],
)
class BookViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Book.objects.all().order_by("title")
    serializer_class = BookSerializer


@extend_schema(
    tags=["Book categories"],
)
class BookCategoryViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = BookCategory.objects.all().order_by("name")
    serializer_class = BookCategorySerializer


@extend_schema(
    tags=["Root view"],
)
class CustomApiRootView(APIView):  # type: ignore
    """
    Custom API root view that lists available endpoints.
    """

    # Define a dummy serializer
    class DummySerializer(serializers.Serializer):  # type: ignore
        pass  # No fields, just a placeholder

    # Explicitly tell DRF that this view has no serializer
    @staticmethod
    def get_serializer_class() -> Type[DummySerializer]:
        return CustomApiRootView.DummySerializer

    @staticmethod
    def get(request, *args, **kwargs):  # type: ignore
        return Response(
            {
                "authors": "/authors/",
                "books": "/books/",
                "categories": "/categories/",
                "author-books": "/author/<int:pk>/books/",  # Custom endpoint added
                "schema": "/api/schema/",
                "swagger-ui": "/api/schema/swagger-ui/",
                "redoc": "/api/schema/redoc/",
            }
        )
