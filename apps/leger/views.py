from django.shortcuts import render, HttpResponse
from apps.master.models import Rombel

def add_nilai(request):
  if request.POST:
    data_siswa = request.POST.getlist('siswa')
    data_p = request.POST.getlist('pengetahuan')
    data_k = request.POST.getlist('keterampilan')
    context = {
      'd_s': data_siswa,
      'd_p': data_p,
      'd_k': data_k,
    }
    return render(request, 'add-nilai.html', context)
  else:
    data = Rombel.objects.filter(kelas__nama='XI.RPL-1', arsip=False, tahun=2020).order_by('siswa__NIS')
    context = {
      'data': data
    }
  return render(request, 'add-nilai.html', context)
