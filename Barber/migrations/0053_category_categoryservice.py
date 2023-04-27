# Generated by Django 4.2 on 2023-04-27 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0052_alter_barber_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("hair", "hair"),
                            ("skin", "skin"),
                            ("makeup", "makeup"),
                            ("nail", "nail"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "barber",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="Barber.barber",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CategoryService",
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
                ("service", models.CharField(blank=True, max_length=255)),
                ("price", models.FloatField(default=0)),
                (
                    "servicePic",
                    models.ImageField(
                        default="default_profile.png",
                        null=True,
                        upload_to="Barber/Service",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="Barber.category",
                    ),
                ),
            ],
        ),
    ]
