# Generated by Django 4.2 on 2023-12-08 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_alter_airport_close_time_alter_airport_open_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='origin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='flights.airport'),
            preserve_default=False,
        ),
    ]