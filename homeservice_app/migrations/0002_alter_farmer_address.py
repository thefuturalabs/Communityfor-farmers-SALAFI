# Generated by Django 3.2.15 on 2022-11-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeservice_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='address',
            field=models.TextField(max_length=100),
        ),
    ]
