# Generated by Django 5.1.3 on 2025-01-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_productcodecounter_alter_product_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Price'),
        ),
    ]
