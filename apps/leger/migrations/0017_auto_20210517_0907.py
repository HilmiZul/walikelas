# Generated by Django 2.2.17 on 2021-05-17 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leger', '0016_auto_20210517_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nilai',
            name='siswa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Siswa'),
        ),
    ]
