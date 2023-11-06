import pytest
from user import services as user_services

from rest_framework.test import APIClient


@pytest.fixture
def user():
    user_dc = user_services.UserDataClass(
        first_name="Harry",
        last_name="Potter",
        email="harry@emial.it",
        password="p455word"
    )
    user = user_services.create_user(user_dc=user_dc)

    return user


@pytest.fixture
def client():
    return APIClient()
