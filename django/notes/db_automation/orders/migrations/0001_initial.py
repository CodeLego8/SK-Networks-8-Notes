# Generated by Django 5.1.3 on 2025-01-07 01:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
        ("game_software", "0002_gamesoftwaredescription"),
    ]

    operations = [
        migrations.CreateModel(
            name="Orders",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PENDING", "결제 대기"),
                            ("COMPLETED", "주문 완료"),
                            ("SHIPPING", "배송 중"),
                            ("DELIVERED", "배송 완료"),
                            ("CANCELED", "주문 취소"),
                        ],
                        default="PENDING",
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="account.account",
                    ),
                ),
            ],
            options={
                "db_table": "orders",
            },
        ),
        migrations.CreateModel(
            name="OrdersItems",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.PositiveIntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "game_software",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="game_software.gamesoftware",
                    ),
                ),
                (
                    "orders",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="orders.orders",
                    ),
                ),
            ],
            options={
                "db_table": "orders_items",
            },
        ),
    ]
