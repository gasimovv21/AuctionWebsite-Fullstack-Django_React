# Generated by Django 4.2.1 on 2023-05-11 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0003_alter_user_email_alter_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=70, unique=True, verbose_name='User email'),
        ),
    ]
