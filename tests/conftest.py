from __future__ import annotations

import pytest
import requests
from django.contrib.auth.models import User

from library_api.models import Author
from library_api.models import Book
from library_api.models import BookCategory
from login_api.models import ExtendedUser
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


@pytest.fixture(scope="function")
def token_admin_setup(django_db_blocker, live_server):
    with django_db_blocker.unblock():
        User.objects.create_superuser(username="test_admin", password="test_admin", is_active=True)

    url = f"{live_server.url}/" + "token/"
    data_ = {"username": "test_admin", "password": "test_admin"}
    response = requests.post(url, data=data_)
    token = response.json()["access"]

    yield token


@pytest.fixture(scope="function")
def token_employee_setup(live_server, django_db_blocker):
    with django_db_blocker.unblock():
        ExtendedUser.objects.create_user(username="test_employee", password="test_employee", is_employee=True)

    url = f"{live_server.url}/" + "token/"
    data_ = {"username": "test_employee", "password": "test_employee"}
    response = requests.post(url, data=data_)
    token = response.json()["access"]

    yield token


@pytest.fixture(scope="function")
def token_user_setup(live_server, django_db_blocker):
    with django_db_blocker.unblock():
        ExtendedUser.objects.create_user(username="test_user", password="test_user", is_employee=False)

    url = f"{live_server.url}/" + "token/"
    data_ = {"username": "test_user", "password": "test_user"}
    response = requests.post(url, data=data_)
    token = response.json()["access"]

    yield token
