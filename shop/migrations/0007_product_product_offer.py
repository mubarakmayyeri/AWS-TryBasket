# Generated by Django 4.1.3 on 2022-11-25 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_offer',
            field=models.IntegerField(default=0),
        ),
    ]