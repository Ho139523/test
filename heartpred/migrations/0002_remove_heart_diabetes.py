# Generated by Django 4.2.14 on 2024-08-08 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heartpred', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heart',
            name='diabetes',
        ),
    ]