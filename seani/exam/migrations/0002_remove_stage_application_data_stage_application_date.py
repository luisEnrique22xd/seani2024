# Generated by Django 5.0.2 on 2024-02-20 21:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stage',
            name='application_data',
        ),
        migrations.AddField(
            model_name='stage',
            name='application_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de aplicacion'),
            preserve_default=False,
        ),
    ]