from django.db import models
from apps.pengaturan.models import Umum

class ProgramKeahlian(models.Model):
  nama = models.CharField(max_length=30)
  alias = models.CharField(max_length=5, null=True)
  keterangan = models.TextField()

  def __str__(self):
    return self.nama


class Siswa(models.Model):
  JK_CHOICES = (
    ("L", "L"),
    ("P", "P"),
  )
  NIS = models.CharField(max_length=9)
  NISN = models.CharField(max_length=10)
  nama = models.CharField(max_length=100)
  gender = models.CharField(max_length=1, choices=JK_CHOICES)
  program_keahlian = models.ForeignKey(ProgramKeahlian, on_delete=models.CASCADE, null=True)
  tahun_masuk = models.DateField(null=True)
  foto = models.ImageField(upload_to="siswa/foto/", null=True, blank=True)

  def __str__(self):
    return self.nama


class Mapel(models.Model):
  KELOMPOK_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C1', 'C1'),
    ('C2', 'C2'),
    ('C3', 'C3'),
  )
  KETERANGAN_CHOICES = (
    ("Muatan Nasional", "Muatan Nasional"),
    ("Muatan Kewilayahan", "Muatan Kewilayahan"),
    ("Dasar Bidang Keahlian", "Dasar Bidang Keahlian"),
    ("Dasar Program Keahlian", "Dasar Program Keahlian"),
    ("Muatan Peminatan dan Kejuruan", "Muatan Peminatan dan Kejuruan"),
  )
  KOMPETENSI_KEAHLIAN_CHOICES = (
    ("Semua", "Semua"),
    ("TKI", "TKI"),
    ("RPL", "RPL"),
    ("TKJ", "TKJ"),
    ("TBSM", "TBSM"),
  )
  nama = models.CharField(max_length=50)
  alias = models.CharField(max_length=40, null=True)
  kelompok = models.CharField(max_length=2, choices=KELOMPOK_CHOICES)
  keterangan = models.CharField(max_length=29, choices=KETERANGAN_CHOICES, null=True)
  kkm = models.IntegerField()
  alokasi_waktu = models.IntegerField(null=True)
  kompetensi_keahlian = models.CharField(max_length=5, choices=KOMPETENSI_KEAHLIAN_CHOICES, null=True)

  def __str__(self):
    return self.nama


class Kelas(models.Model):
  KELAS_CHOICES = (
    ("RPL", (
      ("XII.RPL-1", "XII.RPL-1"),
      ("XII.RPL-2", "XII.RPL-2"),
      ("XII.RPL-3", "XII.RPL-3"),
      ("XII.RPL-4", "XII.RPL-4"),
    )),
    ("TKJ", (
      ("XII.TKJ-1", "XII.TKJ-1"),
      ("XII.TKJ-2", "XII.TKJ-2"),
      ("XII.TKJ-3", "XII.TKJ-3"),
      ("XII.TKJ-4", "XII.TKJ-4"),
    ))
  )
  TINGKAT_CHOICE = (
    ('X', 'X'),
    ('XI', 'XI'),
    ('XII', 'XII')
  ) 
  tingkat = models.CharField(max_length=3, choices=TINGKAT_CHOICE, null=True)
  nama = models.CharField(max_length=10, null=True) # siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
  # tahun_ajaran = models.DateField()
  # arsip = models.BooleanField(default=False)

  def __str__(self):
    return self.nama


class Guru(models.Model):
  gender_choices = (
    ('L', 'L'),
    ('P', 'P'),
  )
  LEVEL_CHOICES = (
    ('Non-PNS', 'Non-PNS'),
    ('PNS', 'PNS'),
  )
  NIP = models.CharField(max_length=20)
  nama = models.CharField(max_length=50)
  gender = models.CharField(max_length=1, choices=gender_choices)
  level = models.CharField(max_length=7, choices=LEVEL_CHOICES)
  walikelas = models.ForeignKey(Kelas, on_delete=models.CASCADE, blank=True, null=True)
  tahun_masuk = models.DateField(null=True)
  foto = models.ImageField(upload_to="guru/foto/", null=True, blank=True)
  email = models.EmailField(max_length=60, null=True)
  aktif = models.BooleanField(default=True)

  def __str__(self):
    return self.nama


class Rombel(models.Model):
  kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
  siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
  walikelas = models.ForeignKey(Guru, on_delete=models.CASCADE)
  tahun = models.IntegerField()
  # tahun = models.ForeignKey(Umum, on_delete=models.CASCADE, null=True)
  arsip = models.BooleanField(default=False)

  def __str__(self):
    return self.kelas.nama


class GuruMapel(models.Model):
  kelompok_choices = (
    ('Produktif', 'Produktif'),
    ('Adaptif', 'Adaptif'),
    ('Normatif', 'Normatif'),
  )
  guru = models.ForeignKey(Guru, on_delete=models.CASCADE)
  kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
  mapel = models.ForeignKey(Mapel, on_delete=models.CASCADE)
  kelompok = models.CharField(max_length=9, choices=kelompok_choices, null=True)

  def __str__(self):
    return self.guru.nama
