# Generated by Django 4.2.1 on 2023-05-17 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0003_iteminauction_item_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iteminauction',
            name='item_owner',
            field=models.ForeignKey(blank=True, choices=[], help_text='Determine which user the item belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='items_api.user', verbose_name='Owner name'),
        ),
    ]