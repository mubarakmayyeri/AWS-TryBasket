# Generated by Django 4.1.3 on 2022-11-05 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_sub_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_category',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
