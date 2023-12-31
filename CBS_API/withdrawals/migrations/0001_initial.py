# Generated by Django 4.1.7 on 2023-09-28 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Customers", "0002_alter_customers_ghana_card_number"),
    ]

    operations = [
        migrations.CreateModel(
            name="Withdrawals",
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
                ("amount", models.FloatField(blank=True, default=0.0, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="withdrawals",
                        to="Customers.customers",
                    ),
                ),
            ],
        ),
    ]
