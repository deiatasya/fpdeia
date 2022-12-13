from django.forms import ModelForm
from dashboard.models import Barang
from django import forms
from dashboard.models import makanan, minuman


class FormBarang(ModelForm):
    class meta :
        model=Barang
        
        fields='__all__'

        Widgets = {
            'kodebrg': forms.TextInput ({'class':'form-control'}),
            'nama':forms.TextInput ({'class':'form-control'}),
            'stok': forms.TextInput ({'class':'form-contro'}),
            'harga': forms.TextInput ({'class':'form-contro'}),
            'link_gbr': forms.TextInput ({'class':'form-contro'}),
            'jenis_id': forms.TextInput ({'class':'form-contro'}),
        }
        
    