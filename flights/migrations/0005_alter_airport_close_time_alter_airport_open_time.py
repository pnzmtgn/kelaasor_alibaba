# Generated by Django 4.2 on 2023-12-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_alter_airport_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='close_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='airport',
            name='open_time',
            field=models.TimeField(),
        ),
    ]