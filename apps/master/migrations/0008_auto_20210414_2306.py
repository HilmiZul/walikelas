# Generated by Django 2.2.17 on 2021-04-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0007_auto_20210414_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='guru',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='guru/foto/'),
        ),
        migrations.AddField(
            model_name='siswa',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='siswa/foto/'),
        ),
        migrations.AlterField(
            model_name='guru',
            name='level',
            field=models.CharField(choices=[('Non-PNS', 'Non-PNS'), ('PNS', 'PNS')], max_length=7),
        ),
    ]
