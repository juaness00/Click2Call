# Generated by Django 2.1.5 on 2022-08-23 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Config', '0004_auto_20220823_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plan',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]