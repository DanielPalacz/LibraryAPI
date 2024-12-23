from __future__ import annotations

import requests


def test_endpoints_drf_root(live_server):
    url = f"{live_server.url}/"
    response = requests.get(url)
    assert response.status_code == 200


def test_endpoints_get_categories(live_server):
    url = f"{live_server.url}/" + "categories/"
    response = requests.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) == 7


def test_endpoints_post_categories(live_server):
    url = f"{live_server.url}/" + "categories/"
    data = {"name": "NewCategoryAuto"}

    response = requests.post(url, data=data)
    assert response.status_code == 200 or response.status_code == 201

    response_data = response.json()
    assert list(response_data.keys()) == ["id", "name", "parent"]
    assert response_data["name"] == "NewCategoryAuto"
    assert response_data["parent"] is None

    response = requests.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) == 8


def test_endpoints_post_categories_incorrect_category_name(live_server):
    url = f"{live_server.url}/" + "categories/"
    data = {"name": "xx"}

    response = requests.post(url, data=data)
    assert response.status_code == 400
    assert response.reason == "Bad Request"
    assert response.text == '{"name":["Category name should have at least 3 letters."]}'


def test_endpoints_post_two_the_same_categories(live_server):
    url = f"{live_server.url}/" + "categories/"
    data = {"name": "NewCategoryAuto"}

    response = requests.post(url, data=data)
    assert response.status_code == 200 or response.status_code == 201

    response_data = response.json()
    assert list(response_data.keys()) == ["id", "name", "parent"]
    assert response_data["name"] == "NewCategoryAuto"
    assert response_data["parent"] is None

    response = requests.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) == 8

    response = requests.post(url, data=data)
    assert response.status_code == 400
    assert response.reason == "Bad Request"
    assert response.text == '{"name":["book category with this name already exists."]}'


def test_endpoints_get_single_category(live_server):
    url = f"{live_server.url}/" + "categories/"
    response = requests.get(url)
    last_category = response.json()[-1]

    single_category_url = url + str(last_category["id"]) + "/"
    single_category_response = requests.get(single_category_url)
    assert list(single_category_response.json().keys()) == ["id", "name", "parent"]
    assert single_category_response.json()["id"] == last_category["id"]


def test_endpoints_get_single_category_with_parent(live_server):
    url = f"{live_server.url}/" + "categories/"
    response = requests.get(url)
    categories_data = [category["name"] for category in response.json() if category["parent"] is not None]
    assert categories_data == ["Fantasy", "Required book"]


def test_endpoints_post_categories_category_cant_be_own_parent(live_server):
    url = f"{live_server.url}/" + "categories/"
    data = {"name": "NewCategoryAuto"}

    response = requests.post(url, data=data)
    assert response.status_code == 200 or response.status_code == 201

    response_data = response.json()
    assert list(response_data.keys()) == ["id", "name", "parent"]
    assert response_data["name"] == "NewCategoryAuto"
    assert response_data["parent"] is None

    new_category_url = url + str(response_data["id"]) + "/"

    data_update = {"id": response_data["id"], "name": "NewCategoryAuto", "parent": new_category_url}

    single_category_response = requests.put(new_category_url, data=data_update)
    assert single_category_response.status_code == 400
    assert single_category_response.reason == "Bad Request"
    assert single_category_response.text == '{"non_field_errors":["The category can\'t be own parent."]}'


def test_endpoints_update_fully_single_category(live_server):
    url = f"{live_server.url}/" + "categories/"
    response = requests.get(url)
    last_category = response.json()[-1]

    data_update = {"id": last_category["id"], "name": "NewValueFullUpdate", "parent": None}

    single_category_url = url + str(last_category["id"]) + "/"
    single_category_response = requests.put(single_category_url, data=data_update)

    assert list(single_category_response.json()) == ["id", "name", "parent"]

    single_category_response = requests.get(single_category_url)
    assert single_category_response.json() == {
        "id": last_category["id"],
        "name": "NewValueFullUpdate",
        "parent": single_category_response.json()["parent"],
    }


def test_endpoints_update_partially_single_category(live_server):
    url = f"{live_server.url}/" + "categories/"
    response = requests.get(url)
    last_category = response.json()[-1]

    data_update = {"name": "NewValuePartialUpdate"}

    single_category_url = url + str(last_category["id"]) + "/"
    single_category_response = requests.patch(single_category_url, data=data_update)

    assert list(single_category_response.json()) == ["id", "name", "parent"]

    single_category_response = requests.get(single_category_url)
    assert single_category_response.json() == {
        "id": last_category["id"],
        "name": "NewValuePartialUpdate",
        "parent": single_category_response.json()["parent"],
    }


def test_endpoints_delete_category(live_server):
    url = f"{live_server.url}/" + "categories/"
    response = requests.get(url)
    last_category = response.json()[-1]
    single_category_url = url + str(last_category["id"]) + "/"
    single_category_response = requests.delete(single_category_url)
    assert single_category_response.status_code == 204

    single_category_response = requests.get(single_category_url)
    assert single_category_response.status_code == 404
