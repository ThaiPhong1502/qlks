
"""
Definition of models.
"""

from django.db import models


# Create your models here.



class LOAIPHONG(models.Model):
    TenLoaiPhong=models.CharField(max_length=100)
    
    def __str__(self):
        return self.TenLoaiPhong






class PHONG(models.Model):
    IDloaiphong=models.ForeignKey(LOAIPHONG,on_delete=models.CASCADE)
    TenPhong = models.CharField(max_length=100)
    NgayThue=models.DateTimeField()
    NgayTra=models.DateTimeField()
    DonGia = models.IntegerField()
    TinhTrang=models.CharField(max_length=100)

    def __str__(self):
        return self.TenPhong









class LOAIKHACHHANG(models.Model):
    TenLoaiKhachHang=models.CharField(max_length=100)

    def __str__(self):
        return self.TenLoaiKhachHang







class KHACHHANG(models.Model):
    IDLoaiKhachHang=models.ForeignKey(LOAIKHACHHANG,on_delete=models.CASCADE)
    IDphong=models.ForeignKey(PHONG,on_delete=models.CASCADE)
    TenKhachHang=models.CharField(max_length=100)
    CMND=models.CharField(max_length=100)
    SDT=models.IntegerField()
    DiaChi=models.CharField(max_length=100)

    def __str__(self):
        return self.TenKhachHang









class HOADON(models.Model):
    IDphong=models.ForeignKey(PHONG,on_delete=models.CASCADE)
    IDKhachHang=models.ForeignKey(KHACHHANG,on_delete=models.CASCADE)
    NgayThanhToan = models.DateTimeField()
    SoDem = models.IntegerField()
    TongTien = models.IntegerField()

    def __str__(self):
        return self.IDKhachHang





class THONGKEDOANHTHU(models.Model):
    IDHoaDon=models.ForeignKey(HOADON,on_delete=models.CASCADE)
    IDLoaiPhong=models.ForeignKey(LOAIPHONG,on_delete=models.CASCADE)
    DoanhThu=models.IntegerField()
    Thang=models.DateTimeField()

    def __str__(self):
        return self.IDLoaiPhong