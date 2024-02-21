# Generated by Django 5.0.2 on 2024-02-20 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(verbose_name='Etapa')),
                ('application_data', models.DateTimeField(verbose_name='Fecha de aplicacion')),
            ],
            options={
                'verbose_name': 'etapa',
                'verbose_name_plural': 'etapas',
            },
        ),
    ]
