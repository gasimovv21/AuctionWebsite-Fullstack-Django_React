# Generated by Django 4.2.1 on 2023-05-17 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemInAuction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=60, verbose_name='Item name')),
                ('price', models.PositiveIntegerField(verbose_name='Price of item')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]