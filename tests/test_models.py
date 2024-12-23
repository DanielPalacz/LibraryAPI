from __future__ import annotations

import django.db.utils
import pytest
from django.db import connection

from library_api.models import Author
from library_api.models import Book
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


@pytest.mark.django_db()
def test_book():
    book_item = Book.objects.get(title="The Idiot")
    assert book_item.title == "The Idiot"
    assert "Fyodor Dostoevsky" in str(book_item.author)
    assert [category.name for category in book_item.category.all()] == ["Classic"]


@pytest.mark.django_db()
def test_book_with_two_categories():
    book_item = Book.objects.get(title="All About the Bullerby Children")
    assert book_item.title == "All About the Bullerby Children"
    assert "Astrid Lindgren" in str(book_item.author)
    assert [category.name for category in book_item.category.all()] == ["For children", "Required book"]


@pytest.mark.django_db()
def test_author_not_exists():
    with pytest.raises(Author.DoesNotExist):
        Author.objects.get(first_name="John", last_name="Dove")


@pytest.mark.django_db()
def test_author_duplicate():
    with pytest.raises(django.db.utils.IntegrityError) as e:
        author_object1 = Author(first_name="John", last_name="Dove")
        author_object1.save()
        author_object2 = Author(first_name="John", last_name="Dove")
        author_object2.save()

    assert "UNIQUE constraint failed: library_api_author.first_name, library_api_author.last_name" == str(e.value)
