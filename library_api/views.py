from __future__ import annotations

from typing import Type

from django.db.models import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import serializers  # type: ignore
from rest_framework import viewsets
from rest_framework.filters import SearchFilter  # type: ignore
from rest_framework.generics import ListAPIView  # type: ignore
from rest_framework.pagination import PageNumberPagination  # type: ignore
from rest_framework.permissions import AllowAny  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework.views import APIView  # type: ignore

from .models import Author
from .models import Book
from .models import BookCategory
from .serializers import AuthorSerializer
from .serializers import BookCategorySerializer
from .serializers import BookSerializer


@extend_schema(
    tags=["Authors"],
)
class AuthorViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Author.objects.all().order_by("last_name")
    serializer_class = AuthorSerializer


@extend_schema(
    tags=["Author books"],
    responses=BookSerializer(many=True),
)
class AuthorBooksView(ListAPIView):  # type: ignore
    """The given Author books."""

    serializer_class = BookSerializer

    def get_queryset(self) -> QuerySet:  # type: ignore
        user_id = self.kwargs["pk"]
        # Ensure the author exists or raise a 404
        if not Author.objects.filter(pk=user_id).exists():
            raise Http404("Author not found")

        # Optimize the query for related books
        return Book.objects.select_related("author").filter(author__pk=user_id)


class BookPagination(PageNumberPagination):  # type: ignore
    page_size = 5  # Default 5 books on the page
    page_size_query_param = "page_size"  # Allows to User modify number of elements on the page


@extend_schema(
    tags=["Books"],
)
class BookViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Book.objects.all().order_by("title")
    serializer_class = BookSerializer
    pagination_class = BookPagination
    filter_backends = (SearchFilter,)
    search_fields = ["title", "author__last_name"]


@extend_schema(
    tags=["Book categories"],
)
class BookCategoryViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = BookCategory.objects.all().order_by("name")
    serializer_class = BookCategorySerializer


@extend_schema(
    tags=["Category books"],
    responses=BookSerializer(many=True),
)
class CategoryBooksView(ListAPIView):  # type: ignore
    """The given Book category books."""

    serializer_class = BookSerializer

    def get_queryset(self) -> QuerySet:  # type: ignore
        category_id = self.kwargs["pk"]
        book_category = get_object_or_404(BookCategory, pk=category_id)
        return book_category.books.all()


@extend_schema(
    tags=["Root view"],
)
class CustomApiRootView(APIView):  # type: ignore
    """
    Custom DRF API root view listing available endpoints.
    """

    permission_classes = [AllowAny]  # This turns off authentication

    # Define a dummy serializer
    class DummySerializer(serializers.Serializer):  # type: ignore
        pass  # No fields, just a placeholder

    # It is to satisfy some documentation relationships
    @staticmethod
    def get_serializer_class() -> Type[DummySerializer]:
        return CustomApiRootView.DummySerializer

    @staticmethod
    def get(request, *args, **kwargs):  # type: ignore
        response = Response(
            {
                "drf-root": "/",
                "authors": "/authors/",
                "books": "/books/",
                "categories": "/categories/",
                "users": "/users/",
                "author-books": "/author/<int:pk>/books/",  # Custom endpoint added
                "category-books": "/category/<int:pk>/books/",  # Custom endpoint added
                "schema": "/api/schema/",
                "swagger-ui": "/api/schema/swagger-ui/",
                "redoc": "/api/schema/redoc/",
            }
        )

        # response.set_cookie('test-cookie', 'test', max_age=100, httponly=True, samesite="Strict")

        return response
