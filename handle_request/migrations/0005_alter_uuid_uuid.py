# Generated by Django 3.2.3 on 2021-05-27 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle_request', '0004_alter_uuid_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uuid',
            name='uuid',
            field=models.CharField(default='e6ef27a259cb49d2a9cbd779dba5e85c', max_length=35),
        ),
    ]