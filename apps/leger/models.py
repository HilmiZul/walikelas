from django.db import models
from apps.master.models import Mapel, Kelas, ProgramKeahlian, Siswa
from apps.pengaturan.models import Umum

class Nilai(models.Model):
  JUDUL_CHOICES = (
    ('Harian', 'Harian'),
    ('PTS', 'Penilaian Tengah Semester'),
    ('PAS', 'Penilaian Akhir Semester'),
    ('PAT', 'Penilaian Akhir Tahun'),
    ('Rapot', 'Nilai Rapot'),
  )
  judul = models.CharField(max_length=30, choices=JUDUL_CHOICES, null=True)
  tanggal = models.DateTimeField(auto_now_add=True, null=True)
  mata_pelajaran = models.ForeignKey(Mapel, on_delete=models.CASCADE, null=True)  # diambil dari Guru Mapel yang sedang login 
  #kkm = models.IntegerField(null=True)                                            # diisi manual / dari Mapel?
  kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE, null=True)           # diinput dari obj Kelas
  semester = models.ForeignKey(Umum, on_delete=models.CASCADE, null=True)         # diambil dari pengaturan Umum
  siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)                      # dari obj Siswa
  pengetahuan = models.IntegerField()
  keterampilan = models.IntegerField()

  def __str__(self):
    return self.siswa.nama


class Leger(models.Model):
  SIKAP_CHOICES = (
    ("A", "Amat Baik"),
    ("B", "Baik"),
    ("C", "Cukup"),
    ("D", "Kurang"),
  )
  nilai = models.ForeignKey(Nilai, on_delete=models.CASCADE)
  nilai_s = models.CharField(max_length=1, choices=SIKAP_CHOICES) # NILAI SIKAP

  def __str__(self):
    return self.nilai.siswa.nama
