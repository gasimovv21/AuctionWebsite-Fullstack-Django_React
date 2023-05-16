# Generated by Django 4.2.1 on 2023-05-11 01:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='User name'),
        ),
    ]