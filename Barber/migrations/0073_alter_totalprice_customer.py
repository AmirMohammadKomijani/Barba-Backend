# Generated by Django 4.2 on 2023-05-14 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Customer", "0028_alter_customer_credit"),
        ("Barber", "0072_remove_orderservices_totalprice_totalprice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="totalprice",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customerTotal",
                to="Customer.customer",
            ),
        ),
    ]