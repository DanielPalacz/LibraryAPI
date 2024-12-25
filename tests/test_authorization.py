from __future__ import annotations

import pytest
import requests


@pytest.mark.authorization
def test_admin(token_admin_setup):
    response = requests.get("http://127.0.0.1:8000/users/", headers={"Authorization": f"Bearer {token_admin_setup}"})
    assert response.status_code == 200
