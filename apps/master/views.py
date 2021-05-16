from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from .models import Guru, Siswa, Rombel, GuruMapel
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Count

@login_required(login_url=settings.LOGIN_URL)
def home(request):
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
  return render(request, 'home.html', context)


@login_required(login_url=settings.LOGIN_URL)
def myclass(request):
  rombel = Rombel.objects.filter(walikelas__email=request.user.email)
  guru = Guru.objects.get(email=request.user.email)
  L = Rombel.objects.filter(walikelas__email=request.user.email, siswa__gender='L').count()
  P = Rombel.objects.filter(walikelas__email=request.user.email, siswa__gender='P').count()
  context = {
    'rombel': rombel,
    'guru': guru,
    'L': L,
    'P': P
  }
  return render(request, 'kelas.html', context)
