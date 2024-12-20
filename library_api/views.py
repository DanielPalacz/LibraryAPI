from __future__ import annotations

from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets  # type: ignore
from rest_framework.generics import ListAPIView  # type: ignore

from .models import Author
from .models import Book
from .models import BookCategory
from .serializers import AuthorSerializer
from .serializers import BookCategorySerializer
from .serializers import BookSerializer

# from django.shortcuts import render


class AuthorViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Author.objects.all().order_by("last_name")
    serializer_class = AuthorSerializer


@extend_schema(
    tags=["Books"],
    description="The given Author books.",
    responses=BookSerializer(many=True),
)
class AuthorBooksView(ListAPIView):  # type: ignore
    serializer_class = BookSerializer

    def get_queryset(self) -> QuerySet:  # type: ignore
        user_id = self.kwargs["pk"]
        return Book.objects.filter(id=user_id)


class BookViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Book.objects.all().order_by("title")
    serializer_class = BookSerializer


class BookCategoryViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = BookCategory.objects.all().order_by("name")
    serializer_class = BookCategorySerializer
