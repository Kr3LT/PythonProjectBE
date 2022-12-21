from app.models import ChiTietHoaDons
from app import db


def GetByMaHoaDon(maHoaDon):
    return ChiTietHoaDons.query.filter(ChiTietHoaDons.MaHoaDon == maHoaDon).all()


def Create(maHoaDon, maSanPham, soLuong, donGia):
    chiTietHoaDon = ChiTietHoaDons(MaHoaDon = maHoaDon, MaSanPham = maSanPham, SoLuong = soLuong, DonGia = donGia)
    db.session.add(chiTietHoaDon)
    db.session.commit()
    return chiTietHoaDon


def Update(maChiTietHoaDon, maHoaDon, maSanPham, soLuong, donGia):
    chiTietHoaDon = ChiTietHoaDons.query.filter(ChiTietHoaDons.MaChiTietHoaDon == maChiTietHoaDon).first()
    chiTietHoaDon.MaHoaDon = maHoaDon
    chiTietHoaDon.MaSanPham = maSanPham
    chiTietHoaDon.SoLuong = soLuong
    chiTietHoaDon.DonGia = donGia
    db.session.commit()
    return chiTietHoaDon


def Delete(maChiTietHoaDon):
    chiTietHoaDon = ChiTietHoaDons.query.filter(ChiTietHoaDons.MaChiTietHoaDon == maChiTietHoaDon).first()
    db.session.delete(chiTietHoaDon)
    db.session.commit()


def TongTien():
    chiTiets = ChiTietHoaDons.query.all()
    s = 0
    for chiTiet in chiTiets:
        s = s + chiTiet.SoLuong * chiTiet.DonGia
    return s