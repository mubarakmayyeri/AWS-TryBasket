# Generated by Django 4.1.3 on 2022-11-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_sub_category_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(upload_to='photos/categories'),
        ),
    ]
