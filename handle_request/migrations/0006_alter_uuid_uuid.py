# Generated by Django 3.2.3 on 2021-05-27 03:41

from django.db import migrations, models
import handle_request.models


class Migration(migrations.Migration):

    dependencies = [
        ('handle_request', '0005_alter_uuid_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uuid',
            name='uuid',
            field=models.CharField(default=handle_request.models.unique_uuid, max_length=35),
        ),
    ]
