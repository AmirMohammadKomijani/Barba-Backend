# Generated by Django 4.2.1 on 2023-05-29 12:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0077_barber_expire_date_alter_barberpremium_month"),
    ]

    operations = [
        migrations.AlterField(
            model_name="barberpremium",
            name="barber",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Barber.barber",
            ),
        ),
        migrations.AlterField(
            model_name="barberpremium",
            name="expire_date",
            field=models.DateField(default=datetime.date(2023, 6, 29), null=True),
        ),
        migrations.AlterField(
            model_name="barberpremium",
            name="month",
            field=models.IntegerField(
                choices=[
                    (1, "1-month"),
                    (3, "3-month"),
                    (6, "6-month"),
                    (12, "12-month"),
                ],
                default=0,
                null=True,
            ),
        ),
    ]
