# Generated by Django 2.1.5 on 2022-08-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Config', '0008_rename_passwordtoken_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productwebsites',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
