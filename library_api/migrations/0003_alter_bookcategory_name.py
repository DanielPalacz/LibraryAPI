# Generated by Django 5.1.4 on 2024-12-19 22:13
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("library_api", "0002_alter_bookcategory_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookcategory",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
