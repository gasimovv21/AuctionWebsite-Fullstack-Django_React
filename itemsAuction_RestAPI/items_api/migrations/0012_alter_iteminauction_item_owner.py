# Generated by Django 4.2.1 on 2023-05-21 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0011_alter_iteminauction_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iteminauction',
            name='item_owner',
            field=models.ForeignKey(default=None, help_text='Determine which user the item belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='items_api.user', verbose_name='Owner name'),
            preserve_default=False,
        ),
    ]
