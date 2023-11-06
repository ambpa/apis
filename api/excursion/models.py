import datetime

from django.db import models
from django.conf import settings


class Excursion(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="user"
    )

    content = models.TextField(verbose_name="content")

    date_published = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date Published"
    )

    minimum_user = models.IntegerField(verbose_name="minimum_user", default=0)
    maximum_user = models.IntegerField(verbose_name="maximum_user", default=10)

    time_excursion = models.DurationField(verbose_name="durata", default=datetime.timedelta(seconds=0))

    start_time_excursion = models.DateTimeField(verbose_name="partenza", default=None)
    end_booking_time = models.DateTimeField(default=None)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="price"
    )
    meeting_place = models.CharField(verbose_name="meeting_place", max_length=500, default="")
