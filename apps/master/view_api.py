from .models import *
from .serializers import *
from rest_framework import viewsets, generics

class GuruViewset(viewsets.ModelViewSet):
  queryset = Guru.objects.all()
  serializer_class = GuruSerializer

class SiswaViewset(viewsets.ModelViewSet):
  queryset = Siswa.objects.all()
  serializer_class = SiswaSerializer


class RombelViewset(viewsets.ModelViewSet):
  queryset = Rombel.objects.all()
  serializer_class = RombelSerializer


class GuruMapelViewset(viewsets.ModelViewSet):
  queryset = GuruMapel.objects.all()
  serializer_class = GuruMapelSerializer

class MapelViewset(viewsets.ModelViewSet):
  queryset = Mapel.objects.all()
  serializer_class = MapelSerializer
