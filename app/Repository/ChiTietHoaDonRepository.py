from app.models import ChiTietHoaDons
from app import db


def GetAll():
    return ChiTietHoaDons.query.all()


def GetByMaHoaDon(maHoaDon):
    return ChiTietHoaDons.query.filter(ChiTietHoaDons.MaHoaDon == maHoaDon).all()


def Create(maHoaDon, maChiTietSanPham, soLuong, donGia):
    chiTietHoaDon = ChiTietHoaDons(MaHoaDon = maHoaDon, MaChiTietSanPham = maChiTietSanPham, SoLuong = soLuong, DonGia = donGia)
    db.session.add(chiTietHoaDon)
    db.session.commit()
    return chiTietHoaDon


def Update(maChiTietHoaDon, maHoaDon, maChiTietSanPham, soLuong, donGia):
    chiTietHoaDon = ChiTietHoaDons.query.filter(ChiTietHoaDons.MaChiTietHoaDon == maChiTietHoaDon).first()
    chiTietHoaDon.MaHoaDon = maHoaDon
    chiTietHoaDon.MaChiTietSanPham = maChiTietSanPham
    chiTietHoaDon.SoLuong = soLuong
    chiTietHoaDon.DonGia = donGia
    db.session.commit()
    return chiTietHoaDon


def Delete(maChiTietHoaDon):
    chiTietHoaDon = ChiTietHoaDons.query.filter(ChiTietHoaDons.MaChiTietHoaDon == maChiTietHoaDon).first()
    db.session.delete(chiTietHoaDon)
    db.session.commit()
    return "Deleted"


def TongTien(maHoaDon):
    chiTiets = ChiTietHoaDons.query.filter(ChiTietHoaDons.MaHoaDon == maHoaDon).all()
    s = 0
    for chiTiet in chiTiets:
        s = s + chiTiet.SoLuong * chiTiet.DonGia
    return s
