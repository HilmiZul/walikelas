from django.contrib import admin
from .models import Identitas, Umum, Rapor

class IdAdmin(admin.ModelAdmin):
  list_display = ['nama_sekolah', 'alamat']

class UmumAdmin(admin.ModelAdmin):
  list_display = ['tahun_ajaran', 'semester']

class RaporAdmin(admin.ModelAdmin):
  list_display = ['titimangsa', 'tahun_semester']


admin.site.register(Identitas, IdAdmin)
admin.site.register(Umum, UmumAdmin)
admin.site.register(Rapor, RaporAdmin)
