# Generated by Django 5.1.4 on 2024-12-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("url", models.URLField(blank=True, null=True)),
                ("text", models.CharField(blank=True, max_length=255, null=True)),
                ("drive_range", models.FloatField(blank=True, null=True)),
                ("charge_time", models.FloatField(blank=True, null=True)),
                ("power", models.FloatField(blank=True, null=True)),
                ("전장", models.IntegerField(blank=True, null=True)),
                ("전폭", models.IntegerField(blank=True, null=True)),
                ("전고", models.IntegerField(blank=True, null=True)),
                ("축거", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "car",
            },
        ),
    ]
