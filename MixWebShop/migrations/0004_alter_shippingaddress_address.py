# Generated by Django 3.2.4 on 2021-06-29 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MixWebShop', '0003_alter_shippingaddress_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='address',
            field=models.TextField(default='', max_length=100),
        ),
    ]
