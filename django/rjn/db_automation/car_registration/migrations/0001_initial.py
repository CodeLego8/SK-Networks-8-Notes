# Generated by Django 5.1.4 on 2025-02-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarRegistration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('지역1', models.CharField(blank=True, max_length=50, null=True)),
                ('등록대수1', models.IntegerField(blank=True, null=True)),
                ('등록대수2', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'car_registration',
            },
        ),
    ]
