# Generated by Django 3.2.15 on 2022-11-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeservice_app', '0002_alter_farmer_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nursery',
            name='nursery_regid',
            field=models.TextField(max_length=10),
        ),
    ]