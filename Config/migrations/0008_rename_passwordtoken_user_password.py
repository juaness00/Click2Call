# Generated by Django 4.1 on 2022-08-24 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Config', '0007_user_passwordtoken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='passwordToken',
            new_name='password',
        ),
    ]
