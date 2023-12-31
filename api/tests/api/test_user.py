import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register_user(client):
    payload = dict(
        first_name="Harry",
        last_name="Potter",
        email="harry@emial.it",
        password="p455word"
    )
    response = client.post("/api/register/", payload)

    data = response.data

    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]
    assert "password" not in data
    assert data["email"] == payload["email"]


@pytest.mark.django_db
def test_login_user(user, client):

    response = client.post("/api/login/", dict(email="harry@emial.it", password="p455word"))

    assert response.status_code ==200


@pytest.mark.django_db
def test_login_user_fail(client):
    response = client.post("/api/login/", dict(email="harry@emial.it", password="p455word"))

    assert response.status_code == 403
