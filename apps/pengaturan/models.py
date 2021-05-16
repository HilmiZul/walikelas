from django.db import models

class Identitas(models.Model):
  nama_sekolah = models.CharField(max_length=50)
  alamat = models.TextField()

  def __str__(self):
    return self.nama_sekolah


class Umum(models.Model):
  SEMESTER_CHOICES = (
    ('Ganjil', 'Ganjil'),
    ('Genap', 'Genap'),
  )
  tahun_ajaran = models.IntegerField()
  semester = models.CharField(max_length=6, choices=SEMESTER_CHOICES)

  def __str__(self):
    return self.semester


class Rapor(models.Model):
  tahun_semester = models.ForeignKey(Umum, on_delete=models.CASCADE)
  titimangsa = models.DateField()

  def __str__(self):
    return self.tahun_semester.semester
