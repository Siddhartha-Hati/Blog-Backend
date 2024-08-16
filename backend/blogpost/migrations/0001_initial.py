# Generated by Django 5.0.7 on 2024-07-21 05:25

import blogpost.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["jpg", "jpeg", "png"]
                            ),
                            blogpost.validators.validate_image_size,
                        ],
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("published_date", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
