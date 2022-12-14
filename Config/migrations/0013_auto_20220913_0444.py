# Generated by Django 2.1.5 on 2022-09-13 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Config', '0012_auto_20220913_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='paymentMethod_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Config.PaymentMethod'),
        ),
        migrations.AlterField(
            model_name='client',
            name='paymentNumber',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='plan_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Config.Plan'),
        ),
        migrations.AlterField(
            model_name='client',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Config.Product'),
        ),
    ]
