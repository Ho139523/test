# Generated by Django 5.1 on 2024-09-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_profilemodel_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(default='registration/user_avatars/default-avatar.png', upload_to='registration/user_avatars'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='fname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='lname',
            field=models.CharField(max_length=150, null=True),
        ),
    ]