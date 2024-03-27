# Generated by Django 5.0.3 on 2024-03-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=7),
        ),
    ]
