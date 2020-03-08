from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100, blank=True)
    gender = models.CharField(max_length=1, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)

class golongan_obat(models.Model):
    class Meta:
        verbose_name = 'Golongan Obat'
        verbose_name_plural = 'Golongan Obat'
    golongan = models.CharField(max_length=50,verbose_name = "Golongan")
    def __str__(self):
        return self.golongan
        
class obat(models.Model):
    class Meta:
        verbose_name = 'Obat'
        verbose_name_plural = 'Obat'
    nama_obat = models.CharField(max_length=30,verbose_name = "Nama")
    stok_obat = models.CharField(max_length=10,blank=True, null=True, verbose_name = "Stok")
    harga_beli_box = models.IntegerField(blank=True, null=True, verbose_name = "Harga Beli Box")
    isi_box = models.IntegerField(blank=True, null=True, verbose_name = "Isi Box")
    harga_beli = models.IntegerField(blank=True, null=True, verbose_name = "Harga Beli")
    harga_jual = models.IntegerField(blank=True, null=True, verbose_name = "Harga Jual")
    exp_date = models.DateTimeField(blank=True, null=True, verbose_name='Exp Date')
    apotik = models.CharField(max_length=200,blank=True, null=True, verbose_name = "Apotik")
    last_update = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id_golongan_obat = models.ForeignKey(
        'master.golongan_obat',
        on_delete=models.CASCADE,
        verbose_name='Golongan'
    )
    def __str__(self):
        return self.nama_obat

class jenis_penyakit(models.Model):
    class Meta:
        verbose_name = 'Jenis Penyakit'
        verbose_name_plural = 'Jenis Penyakit'
    jenis = models.CharField(max_length=50,verbose_name = "Jenis Penyakit")
    def __str__(self):
        return self.jenis

class penyakit(models.Model):
    class Meta:
        verbose_name = 'Penyakit'
        verbose_name_plural = 'Penyakit'
    kode = models.CharField(max_length=25,verbose_name = "Kode Penyakit")
    nama = models.CharField(max_length=200,verbose_name = "Nama Penyakit")
    id_jenis_penyakit = models.ForeignKey(
        'master.jenis_penyakit',
        on_delete=models.CASCADE,
        verbose_name='Jenis Penyakit'
    )
    def __str__(self):
        return self.nama


class tindakan(models.Model):
    class Meta:
        verbose_name = 'Jenis Tindakan'
        verbose_name_plural = 'Jenis Tindakan'
    jenis_tindakan=models.CharField(max_length=255,verbose_name = "Jenis Tindakan")
    def __str__(self):
        return self.jenis_tindakan
    
class jasa_medis(models.Model):
    class Meta:
        verbose_name = 'Jasa Medis'
        verbose_name_plural = 'Jasa Medis'
    jenis_pelayanan = models.CharField(max_length=200,verbose_name = "Jenis Pelayanan")
    jasa_sarana = models.IntegerField(blank=True, null=True, verbose_name = "Jasa Sarana")
    jasa_pembinaan = models.IntegerField(blank=True, null=True, verbose_name = "Jasa Pembinaan")
    jasa_pelayanan = models.IntegerField(blank=True, null=True, verbose_name = "Jasa Pelayanan")
    tarif_total = models.IntegerField(blank=True, null=True, verbose_name = "Total")
    id_jenis_penyakit = models.ForeignKey(
        'master.tindakan',
        on_delete=models.CASCADE,
        verbose_name='Tindakan'
    )
    def __str__(self):
        return self.jenis_pelayanan
