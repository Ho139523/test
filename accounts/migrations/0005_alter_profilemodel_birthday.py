# Generated by Django 4.2.14 on 2024-08-27 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profilemodel_background_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='birthday',
            field=models.DateField(),
        ),
    ]
