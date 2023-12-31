import dataclasses
import datetime
import jwt
from typing import TYPE_CHECKING
from django.conf import settings
from . import models

if TYPE_CHECKING:
    from .models import User


@dataclasses.dataclass
class UserDataClass:
    first_name: str
    last_name: str
    email: str
    password: str = None
    id: int = None
    is_staff: bool = False

    @classmethod
    def from_instance(cls, user: "User") -> "UserDataClass":
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            id=user.id,
            is_staff=user.is_staff,

        )


def create_user(user_dc: "UserDataClass") -> "UserDataClass":
    instance = models.User(
        first_name=user_dc.first_name, last_name=user_dc.last_name, email=user_dc.email, is_staff=user_dc.is_staff
    )
    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()

    return UserDataClass.from_instance(instance)


def user_email_selector(email: str) -> "User":
    user = models.User.objects.filter(email=email).first()

    return user


def create_token(user_id: int) -> str:
    payload = dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        iat=datetime.datetime.utcnow(),
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

    return token


@dataclasses.dataclass
class BlackListedTokenDataClass:
    user: UserDataClass = None
    id: int = None
    timestamp: datetime.datetime = None
    token: str = None
    @classmethod
    def from_instance(cls, blacklistedtoken_model: "BlackListedToken") -> "BlackListedToken":
        return cls(
            token=blacklistedtoken_model.token,
            user=blacklistedtoken_model.user,
            id=blacklistedtoken_model.id,
            timestamp=blacklistedtoken_model.timestamp
        )

def create_blacklistedtoken(user, token, blacklistedtoken: "BlackListedToken") -> "BlackListedToken":
    blacklistedtoken_create = models.BlackListedToken.objects.create(
        token=token,
        user=user,
        id=blacklistedtoken.id,
        timestamp=blacklistedtoken.timestamp
    )
    return BlackListedTokenDataClass.from_instance(blacklistedtoken_model=blacklistedtoken_create)
