from __future__ import annotations

import pytest

from library_api.models import Author
from library_api.models import Book
from library_api.models import BookCategory
from tests.populate_db import run_all


@pytest.fixture(scope="function", autouse=True)
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        run_all()

    yield

    with django_db_blocker.unblock():
        Author.objects.all().delete()
        Book.objects.all().delete()
        BookCategory.objects.all().delete()
