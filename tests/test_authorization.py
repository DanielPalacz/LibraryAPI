from __future__ import annotations

import pytest
import requests


@pytest.mark.authorization
def test_admin(token_admin_setup, live_server):
    url = f"{live_server.url}/" + "users/"
    response = requests.get(url, headers={"Authorization": f"Bearer {token_admin_setup}"})
    assert response.status_code == 200


@pytest.mark.authorization
def test_employee(token_employee_setup, live_server):
    url = f"{live_server.url}/" + "users/"
    response = requests.get(url, headers={"Authorization": f"Bearer {token_employee_setup}"})
    assert response.status_code == 403
    data_ = {"username": "user_test", "email": "user_test@example.com", "password": "pass1111", "is_employee": True}

    url = f"{live_server.url}/" + "register/"
    response = requests.post(url, data=data_, headers={"Authorization": f"Bearer {token_employee_setup}"})
    assert response.status_code == 201
    assert response.json() == {"message": "User registered successfully"}


@pytest.mark.authorization
def test_user(token_user_setup, live_server):
    url = f"{live_server.url}/" + "users/"
    response = requests.get(url, headers={"Authorization": f"Bearer {token_user_setup}"})
    assert response.status_code == 403
    data_ = {"username": "user_test", "email": "user_test@example.com", "password": "pass1111", "is_employee": True}

    url = f"{live_server.url}/" + "register/"
    response = requests.post(url, data=data_, headers={"Authorization": f"Bearer {token_user_setup}"})
    assert response.status_code == 403
    assert response.json() == {"detail": "You do not have permission to perform this action."}
