import imp
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import produk
from dashboard.views import produk, tambah_barang,Barang_view, makanan_view, minuman_view
def coba1(request): 
    return HttpResponse('Selamat Sore...')

def coba2(request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request, 'index.html',konteks)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path ('',coba2, name='coba2'),
    path ('produk/',produk, name='produk'),
    path('addbrg/', tambah_barang, name='addbrg'),
    path('brgview/', Barang_view, name='brgview'),
    path('makanan/', makanan_view, name='makanan'),
    path('minuman/', minuman_view, name='minuman'),
]
