# Generated by Django 4.2.2 on 2023-06-25 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LuxeGems', '0010_remove_jewelry_jewelry_id_jewelry_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewelry',
            name='available',
            field=models.BooleanField(null=True),
        ),
    ]
