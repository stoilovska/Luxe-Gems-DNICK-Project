# Generated by Django 4.2.2 on 2023-06-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LuxeGems', '0013_alter_jewelry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewelry',
            name='image',
            field=models.ImageField(upload_to='jewelry/'),
        ),
    ]
