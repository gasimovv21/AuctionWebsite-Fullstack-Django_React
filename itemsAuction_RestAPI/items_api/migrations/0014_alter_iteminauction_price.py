# Generated by Django 4.2.1 on 2023-05-26 01:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0013_alter_iteminauction_item_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iteminauction',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Price of item'),
        ),
    ]
