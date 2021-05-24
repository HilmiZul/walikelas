from django.urls import path
from .views import *

urlpatterns = [
  path('kelas/', myclass, name="myclass"),

  path('pengaturan/<int:id>', pengaturan_profil, name="pengaturan_profil"),
]