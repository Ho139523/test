# Generated by Django 5.1.3 on 2025-01-19 13:52

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_profilemodel_seller_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='settings_menu',
            field=models.JSONField(blank=True, default=accounts.models.ProfileModel.default_settings_menu),
        ),
    ]
