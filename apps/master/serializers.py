from django.db.models import fields
from .models import *
from rest_framework import serializers

class GuruSerializer(serializers.ModelSerializer):
  walikelas_nama = serializers.CharField(source='walikelas.nama')
  class Meta:
    model = Guru
    fields = [
      'id', 'NIP', 'nama', 'gender', 
      'level', 'tahun_masuk', 'foto', 'email', 
      'walikelas_nama', 'walikelas', 'aktif'
    ]

class SiswaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Siswa
    fields = '__all__'

class RombelSerializer(serializers.ModelSerializer):
  kelas_nama = serializers.CharField(source='kelas.nama')
  siswa_nama = serializers.CharField(source='siswa.nama')
  siswa_program_ahli = serializers.CharField(source='siswa.program_keahlian')
  walikelas_nama = serializers.CharField(source='walikelas.nama')
  walikelas_email = serializers.CharField(source='walikelas.email')
  gender = serializers.CharField(source='siswa.gender')
  foto = serializers.CharField(source='siswa.foto')
  nis = serializers.CharField(source='siswa.NIS')
  class Meta:
    model = Rombel
    fields = [
      'id', 'kelas', 'kelas_nama', 'nis', 'siswa_id', 'siswa_nama', 'siswa_program_ahli',
      'walikelas_id', 'walikelas_nama', 'tahun', 'arsip', 'gender', 'foto', 'walikelas_email',
    ]


class GuruMapelSerializer(serializers.ModelSerializer):
  kelas_nama = serializers.CharField(source='kelas.nama')
  guru_nama = serializers.CharField(source='guru.nama')
  foto = serializers.CharField(source='guru.foto')
  mapel_nama = serializers.CharField(source='mapel.nama')
  email = serializers.CharField(source='guru.email')
  class Meta:
    model = GuruMapel
    fields = [
      'id', 'guru_id', 'guru_nama', 'kelas_id', 'foto',
      'kelas_nama', 'mapel_id', 'mapel_nama', 'kelompok', 'email'
    ]


class MapelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mapel
    fields = '__all__'