from enum import auto
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import modelform_factory

# Create your models here.
class  Jenis (models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def  __str__(self):
        return self.nama

class Barang (models.Model):
    kodebrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    Jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{}. {}. {} {}".format(self.kodebrg,self.nama,self.stok,self.harga)

class makanan (models.Model):
    kode=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{}. {}. {}. {}".format(self.kode,self.nama,self.stok,self.harga, self.jenis_id)  


class minuman (models.Model):
    kode=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{}. {}. {}. {}".format(self.kode,self.nama,self.stok,self.harga, self.jenis_id)  

