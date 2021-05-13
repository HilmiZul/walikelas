from django.contrib import admin
from .models import *

class GuruAdmin(admin.ModelAdmin):
  list_display = ['nama', 'gender', 'walikelas', 'aktif']
  list_filter = ('gender', 'aktif',)
  search_fields = ['nama']
  list_per_page = 20

class MapelAdmin(admin.ModelAdmin):
  list_display = ['nama', 'kelompok', 'kkm']
  list_filter = ('kelompok', 'keterangan',)
  list_per_page = 20

class SiswaAdmin(admin.ModelAdmin):
  list_display = ['NIS', 'nama', 'gender', 'program_keahlian']
  list_filter = ('gender', 'program_keahlian',)
  search_fields = ['nama']
  list_per_page = 20

class KelasAdmin(admin.ModelAdmin):
  list_display = ['nama']
  list_per_page = 20

class RombelAdmin(admin.ModelAdmin):
  list_display = ['siswa', 'kelas', 'walikelas', 'tahun', 'arsip']
  list_filter = ('kelas', 'tahun',)
  search_fields = ['siswa__nama', 'walikelas__nama']
  list_per_page = 36

class GuruMapelAdmin(admin.ModelAdmin):
  list_display = ['guru', 'kelas', 'mapel', 'kelompok']
  list_filter = ('kelas', 'mapel', 'kelompok',)
  search_fields = ['mapel', 'guru']
  list_per_page = 20

admin.site.register(Siswa, SiswaAdmin)
admin.site.register(Guru, GuruAdmin)
admin.site.register(Mapel, MapelAdmin)
admin.site.register(ProgramKeahlian)
admin.site.register(Kelas)
admin.site.register(Rombel, RombelAdmin)
admin.site.register(GuruMapel, GuruMapelAdmin)
