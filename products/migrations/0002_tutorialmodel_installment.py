# Generated by Django 4.2.14 on 2024-10-05 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialmodel',
            name='installment',
            field=models.BooleanField(default=False, verbose_name='Installment Purchase'),
        ),
    ]
