# Generated by Django 2.2.17 on 2021-04-12 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leger', '0007_auto_20210412_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leger',
            name='nilai_s',
            field=models.CharField(choices=[('A', 'Amat Baik'), ('B', 'Baik'), ('C', 'Cukup'), ('D', 'Kurang')], max_length=1),
        ),
    ]
