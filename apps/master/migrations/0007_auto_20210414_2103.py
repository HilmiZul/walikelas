# Generated by Django 2.2.17 on 2021-04-14 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_siswa_tahun_masuk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guru',
            name='walikelas',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='master.Kelas'),
        ),
    ]
