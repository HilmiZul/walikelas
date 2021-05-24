from django import forms
from django.forms import ModelForm
from .models import Guru

class GuruForm(ModelForm):
  class Meta:
    model = Guru
    fields = ['NIP', 'nama', 'gender', 'email', 'foto']
    # exclude = ['tahun_masuk', 'aktif', 'walikelas', 'email', 'level', 'gender']

    widgets = {
      'NIP': forms.TextInput({'class': 'form-control', 'required':'required'}),
      'nama': forms.TextInput({'class': 'form-control', 'required':'required'}),
      'gender': forms.Select({'class':'form-control', 'required':'required'}),
      'level': forms.Select({'class':'form-control', 'required':'required'}),
      'walikelas': forms.Select({'class':'form-control'}),
      'email': forms.EmailInput({'class':'form-control', 'required':'required'}),
      'foto': forms.FileInput({'class':'form-control'})
    }