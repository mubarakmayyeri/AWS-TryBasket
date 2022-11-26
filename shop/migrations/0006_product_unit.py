# Generated by Django 4.1.3 on 2022-11-24 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('Kg', 'Kg'), ('litre', 'litre'), ('pack', 'pack'), ('bottle', 'bottle')], default='Kg', max_length=50),
        ),
    ]
