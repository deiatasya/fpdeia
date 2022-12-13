from django.contrib import admin

# Register your models here.
from .models import Barang, Jenis, makanan, minuman


class kolombarang(admin.ModelAdmin):
    list_display=['kodebrg', 'nama', 'stok', 'harga', 'link_gbr', 'Jenis_id']
    search_fields=['kodebrg','nama']
    list_filter=('Jenis_id',)
    list_per_page= 3

admin.site.register(Barang, kolombarang)
admin.site.register(Jenis)
admin.site.register(makanan)
admin.site.register(minuman)