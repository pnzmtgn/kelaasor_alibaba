# Generated by Django 4.2 on 2023-12-14 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0003_bus_origin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='origin',
        ),
        migrations.AddField(
            model_name='bus',
            name='destination',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bus.terminal'),
            preserve_default=False,
        ),
    ]