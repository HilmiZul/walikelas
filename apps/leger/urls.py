from django.urls import path
from .views import add_nilai

urlpatterns = [
  path('add/', add_nilai, name="add_nilai")
]