# Generated by Django 2.2.17 on 2021-04-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0011_auto_20210414_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guru',
            name='kelompok',
        ),
        migrations.RemoveField(
            model_name='guru',
            name='mata_pelajaran',
        ),
        migrations.AddField(
            model_name='gurumapel',
            name='kelompok',
            field=models.CharField(choices=[('Produktif', 'Produktif'), ('Adaptif', 'Adaptif'), ('Normatif', 'Normatif')], max_length=9, null=True),
        ),
    ]
