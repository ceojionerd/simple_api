# Generated by Django 3.2.3 on 2021-05-27 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle_request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uuid',
            name='uuid',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
