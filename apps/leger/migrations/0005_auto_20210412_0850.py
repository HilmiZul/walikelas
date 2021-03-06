# Generated by Django 2.2.17 on 2021-04-12 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leger', '0004_siswa_kelas'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramKeahlian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='siswa',
            name='program_keahlian',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leger.ProgramKeahlian'),
        ),
    ]
