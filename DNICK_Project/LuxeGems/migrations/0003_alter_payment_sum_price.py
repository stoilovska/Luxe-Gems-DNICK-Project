# Generated by Django 4.2.2 on 2023-06-25 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LuxeGems', '0002_payment_sum_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='sum_price',
            field=models.IntegerField(),
        ),
    ]