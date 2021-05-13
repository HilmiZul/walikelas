from django.urls import path
from .views import *

urlpatterns = [
  path('kelas/', myclass, name="myclass"),
]