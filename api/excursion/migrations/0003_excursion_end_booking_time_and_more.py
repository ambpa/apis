# Generated by Django 4.2.7 on 2023-11-06 14:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("excursion", "0002_excursion_maximum_user_excursion_minimum_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="excursion",
            name="end_booking_time",
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name="excursion",
            name="start_time_excursion",
            field=models.DateTimeField(default=None),
        ),
    ]