# Generated by Django 5.1.3 on 2024-12-10 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarBusinessPricing",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("사업자", models.CharField(blank=True, max_length=50, null=True)),
                ("로밍평균요금", models.FloatField(blank=True, null=True)),
                ("회원평균요금", models.FloatField(blank=True, null=True)),
                ("비회원평균요금", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "car_business_pricing",
            },
        ),
    ]
