# Generated by Django 4.2.14 on 2024-08-08 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='heart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.FloatField()),
                ('anaemia', models.IntegerField()),
                ('creatinine_phosphokinase', models.IntegerField()),
                ('diabetes', models.IntegerField()),
                ('ejection_fraction', models.IntegerField()),
                ('high_blood_pressure', models.IntegerField()),
                ('platelets', models.FloatField()),
                ('serum_creatinine', models.FloatField()),
                ('serum_sodium', models.IntegerField()),
                ('sex', models.IntegerField()),
                ('smoking', models.IntegerField()),
                ('time', models.IntegerField()),
                ('DEATH_EVENT', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]