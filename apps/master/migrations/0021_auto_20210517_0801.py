# Generated by Django 2.2.17 on 2021-05-17 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0020_auto_20210517_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapel',
            name='kelompok',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3')], max_length=2),
        ),
    ]
