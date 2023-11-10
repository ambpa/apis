import dataclasses
import datetime
from typing import TYPE_CHECKING

from django.shortcuts import get_object_or_404
from rest_framework import exceptions

from user import services as user_service
from . import models as excursion_models

if TYPE_CHECKING:
    from models import Excursion
    from user.models import User


@dataclasses.dataclass
class ExcursionDataClass:
    content: str
    maximum_user: int
    minimum_user: int
    end_booking_time: datetime.datetime
    start_time_excursion: datetime.datetime
    time_excursion: datetime.timedelta
    meeting_place: str
    price: float
    date_published: datetime.datetime = None
    user: user_service.UserDataClass = None
    id: int = None

    @classmethod
    def from_instance(cls, excursion_model: "Excursion") -> "ExcursionDataClass":
        return cls(
            content=excursion_model.content,
            date_published=excursion_model.date_published,
            id=excursion_model.id,
            user=excursion_model.user,
            minimum_user=excursion_model.minimum_user,
            maximum_user=excursion_model.maximum_user,
            end_booking_time=excursion_model.end_booking_time,
            start_time_excursion=excursion_model.start_time_excursion,
            time_excursion=excursion_model.time_excursion,
            meeting_place=excursion_model.meeting_place,
            price=excursion_model.price
        )


def create_excursion(user, excursion: "ExcursionDataClass") -> "ExcursionDataClass":
    excursion_create = excursion_models.Excursion.objects.create(
        content=excursion.content,
        user=user,
        maximum_user=excursion.maximum_user,
        minimum_user=excursion.minimum_user,
        end_booking_time=excursion.end_booking_time,
        start_time_excursion=excursion.start_time_excursion,
        time_excursion=excursion.time_excursion,
        meeting_place=excursion.meeting_place,
        price=excursion.price
    )
    return ExcursionDataClass.from_instance(excursion_model=excursion_create)


def get_user_excursion(user: "User") -> list["ExcursionDataClass"]:
    user_excursion = excursion_models.Excursion.objects.filter(user=user)

    return [
        ExcursionDataClass.from_instance(single_excursion) for single_excursion in user_excursion
    ]


def get_user_excursion_detail(user: "User", excursion_id: int) -> "ExcursionDataClass":
    excursion = get_object_or_404(excursion_models.Excursion, pk=excursion_id)
    if user.id != excursion.user.id:
        raise exceptions.PermissionDenied("You're not the user fool")
    return ExcursionDataClass.from_instance(excursion_model=excursion)


def delete_user_excursion(user: "User", excursion_id: int) -> "ExcursionDataClass":
    excursion = get_object_or_404(excursion_models.Excursion, pk=excursion_id)
    if user.id != excursion.user.id:
        raise exceptions.PermissionDenied("You're not the user fool")
    excursion.delete()


def update_user_excursion(user: "User", excursion_id: int, excursion_data: "ExcursionDataClass"):
    excursion = get_object_or_404(excursion_models.Excursion, pk=excursion_id)
    if user.id != excursion.user.id:
        raise exceptions.PermissionDenied("You're not the user fool")

    excursion.content = excursion_data.content
    excursion.save()

    return ExcursionDataClass.from_instance(excursion_model=excursion)
