# Generated by Django 5.0.7 on 2024-08-12 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='toy',
            name='release_data',
            field=models.DateField(default=''),
        ),
        migrations.AddField(
            model_name='toy',
            name='was_included_in_home',
            field=models.BooleanField(default=False),
        ),
    ]
