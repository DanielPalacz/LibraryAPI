from __future__ import annotations

import os

os.environ["DJANGO_SETTINGS_MODULE"] = "LibraryProject.settings"
import django  # noqa: E402

django.setup()

from library_api.models import Author  # noqa: E402
from library_api.models import Book  # noqa: E402
from library_api.models import BookCategory  # noqa: E402


BOOK_CATEGORIES = ["Classic", "Fiction", "Drama", "Horror", "For children"]

AUTHORS = [
    # Classic:
    ["Fyodor", "Dostoevsky", 1821],
    ["William", "Shakespeare", 1564],
    # Fiction
    ["George", "Orwell", 1903],
    # Drama
    ["Sophocles", "-", -497],
    # For Children
    ["Joanne", "Rowling", 1965],
    ["Astrid", "Lindgren", 1907],
]


def __populate_book_subcategories():
    for_children = BookCategory.objects.get(name="For children")
    BookCategory(name="Required book", parent=for_children).save()
    BookCategory(name="Fantasy", parent=for_children).save()


def populate_authors():
    for author in AUTHORS:
        author_obj = Author(first_name=author[0], last_name=author[1], year_of_birth_date=author[2])
        author_obj.save()


def populate_books():
    books = [
        [
            "The Idiot",
            Author.objects.get(first_name="Fyodor", last_name="Dostoevsky"),
            BookCategory.objects.get(name="Classic"),
        ],
        [
            "Hamlet",
            Author.objects.get(first_name="William", last_name="Shakespeare"),
            BookCategory.objects.get(name="Classic"),
        ],
        [
            "Macbeth",
            Author.objects.get(first_name="William", last_name="Shakespeare"),
            BookCategory.objects.get(name="Classic"),
        ],
        [
            "Romeo and Juliet",
            Author.objects.get(first_name="William", last_name="Shakespeare"),
            BookCategory.objects.get(name="Classic"),
        ],
        ["1984", Author.objects.get(first_name="George", last_name="Orwell"), BookCategory.objects.get(name="Fiction")],
        ["Antigone", Author.objects.get(first_name="Sophocles", last_name="-"), BookCategory.objects.get(name="Drama")],
        [
            "Harry Potter",
            Author.objects.get(first_name="Joanne", last_name="Rowling"),
            BookCategory.objects.get(name="For children"),
            BookCategory.objects.get(name="Fantasy"),
        ],
        [
            "All About the Bullerby Children",
            Author.objects.get(first_name="Astrid", last_name="Lindgren"),
            BookCategory.objects.get(name="For children"),
            BookCategory.objects.get(name="Required book"),
        ],
    ]
    for book in books:
        book_obj = Book(title=book[0], author=book[1])

        book_categories = list(book[2:])
        book_obj.save()

        book_obj.category.set(book_categories)

        book_obj.save()


def populate_book_categories():
    for category in BOOK_CATEGORIES:
        BookCategory(name=category).save()

    __populate_book_subcategories()


def run_all():
    populate_book_categories()
    populate_authors()
    populate_books()


if __name__ == "__main__":
    run_all()
