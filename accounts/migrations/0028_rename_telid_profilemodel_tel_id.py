# Generated by Django 5.1.3 on 2025-01-16 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_profilemodel_telid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilemodel',
            old_name='telid',
            new_name='tel_id',
        ),
    ]
