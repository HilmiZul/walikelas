from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from .models import Guru, Siswa, Rombel, GuruMapel
from apps.pengaturan.models import Umum
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Count
from .forms import GuruForm
from django.contrib import messages

@login_required(login_url=settings.LOGIN_URL)
def home(request):
  try:
    guru = Guru.objects.get(email=request.user.email)
    gurumapel = GuruMapel.objects.filter(guru__id=guru.id)
    ngajar = GuruMapel.objects.filter(guru__id=guru.id)
    for k in gurumapel:
      kel = []
      kel.append(k.kelompok)
      kel = kel[0]
    context = {
      'guru': guru,
      'gurumapel': gurumapel,
      'infoNgajar': ngajar,
      'kelompok': kel,
    }
  except:
    context = {
      'guru': None,
      'gurumapel': None,
      'infoNgajar': None,
      'kelompok': None,
    }
  return render(request, 'home.html', context)


@login_required(login_url=settings.LOGIN_URL)
def myclass(request):
  rombel = Rombel.objects.filter(walikelas__email=request.user.email)
  guru = Guru.objects.get(email=request.user.email)
  pengaturan = Umum.objects.get(id=1)
  semester = 0
  if guru.walikelas.tingkat == 'X':
    if pengaturan.semester == 'Ganjil':
      semester = 1
    else:
      semester = 2
  elif guru.walikelas.tingkat == 'XI':
    if pengaturan.semester == 'Ganjil':
      semester = 3
    else:
      semester = 4
  L = Rombel.objects.filter(walikelas__email=request.user.email, siswa__gender='L').count()
  P = Rombel.objects.filter(walikelas__email=request.user.email, siswa__gender='P').count()
  context = {
    'rombel': rombel,
    'guru': guru,
    'L': L,
    'P': P,
    'pengaturan': pengaturan,
    'semester': semester
  }
  return render(request, 'kelas.html', context)


@login_required(login_url=settings.LOGIN_URL)
def pengaturan_profil(request, id):
  guru = Guru.objects.get(id=id)
  if request.POST:
    form = GuruForm(request.POST, request.FILES, instance=guru)
    if form.is_valid():
      form.save()
      messages.success(request, 'Profil berhasil diperbaharui.')
      return redirect('pengaturan_profil', id=id)
  else:
    form = GuruForm(instance=guru)
    template = 'pengaturan-profil.html'
    context = {
      'form': form,
      'guru': guru,
    }
  return render(request, template, context)