# Generated by Django 3.1.3 on 2021-01-08 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210108_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
