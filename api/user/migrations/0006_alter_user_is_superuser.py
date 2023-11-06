# Generated by Django 4.2.7 on 2023-11-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0005_alter_user_is_superuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
    ]
