# Generated by Django 4.2.7 on 2023-11-10 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "excursion",
            "0006_alter_excursion_date_published_alter_excursion_price_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="excursion",
            name="date_last_update",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Date Updated",
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(verbose_name="content_Reservation")),
                (
                    "date_published",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date_published_reservation"
                    ),
                ),
                (
                    "excursion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="excursion.excursion",
                        verbose_name="excursion",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
        ),
    ]
