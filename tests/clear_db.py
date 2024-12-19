from __future__ import annotations

import os

os.environ["DJANGO_SETTINGS_MODULE"] = "LibraryProject.settings"
import django  # noqa: E402

django.setup()

from library_api.models import Author  # noqa: E402
from library_api.models import Book  # noqa: E402
from library_api.models import BookCategory  # noqa: E402


def clean_db_all():
    for author in Author.objects.all():
        author.delete()

    for book in Book.objects.all():
        book.delete()

    for book_cat in BookCategory.objects.all():
        book_cat.delete()


if __name__ == "__main__":
    clean_db_all()
