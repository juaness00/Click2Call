# Generated by Django 4.1 on 2022-08-23 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('refreshRate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('color', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductWebsites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('isAllowedToModifyClients', models.BooleanField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('userType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Config.usertype')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactInfo', models.EmailField(max_length=254)),
                ('paymentMethodId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Config.paymentmethod')),
                ('planId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Config.plan')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Config.product')),
                ('userType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Config.usertype')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Config.usertype')),
            ],
        ),
    ]
