# Generated by Django 4.0 on 2022-01-07 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(null=True),
        ),
    ]
