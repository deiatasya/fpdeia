from django.shortcuts import render
from dashboard.forms import FormBarang
from dashboard.models import Barang, makanan, minuman

# Create your views here.
def tambah_barang(request):
    form=FormBarang
    konteks = {
        'form':form,
    }
    return render(request,'tambah_barang.html',konteks)

def produk(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk.html',konteks)

def Barang_view(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_barang.html',konteks)

def makanan_view(request):
    makanans = makanan.objects.all()

    konteks={
        'makanans': makanans,
    }
    return render(request,'makanan.html',konteks)

def minuman_view(request):
    minumans = minuman.objects.all()

    konteks={
        'minumans': minumans,
    }
    return render(request,'minuman.html',konteks)
