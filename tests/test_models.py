from __future__ import annotations

import pytest
from django.db import connection

from library_api.models import Author
from library_api.models import BookCategory


def test_database_in_memory():
    db_path = connection.settings_dict["NAME"]
    assert "memory" in db_path


@pytest.mark.django_db()
def test_author_books():
    author_object = Author.objects.get(first_name="William", last_name="Shakespeare")
    shakespeare_books = [book.title for book in author_object.books.all()]
    assert "Hamlet" in shakespeare_books
    assert "Macbeth" in shakespeare_books
    assert "Romeo and Juliet" in shakespeare_books


@pytest.mark.django_db()
def test_category_and_subcategory():
    category = BookCategory.objects.get(name="For children")
    subcategories = [subcategory.name for subcategory in category.subcategories.all()]
    assert ["Required book", "Fantasy"] == subcategories
