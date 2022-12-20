from app import db
from datetime import date
from app.models import HoaDons

def GetHoaDonByMaKhachHang(maKhachHang):
    return HoaDons.query.filter(HoaDons.MaKhachHang == maKhachHang).all()


def XacNhanHoaDon(maHoaDon):
    hoaDon = HoaDons.query.filter(HoaDons.MaHoaDon == maHoaDon).first()
    hoaDon.NgayThanhToan = date.today()
    # HoaDons.update().where(HoaDons.MaHoaDon == maHoaDon).values(NgayThanhToan = date.today())
    db.session.commit()
    return hoaDon


def GetById(maHoaDon):
    return HoaDons.query.filter(HoaDons.MaHoaDon == maHoaDon).first()


def Create(maKhachHang, diaChiNhanHang, hinhThucThanhToan, ngayThanhToan):
    hoaDon = HoaDons(MaKhachHang = maKhachHang, DiaChiNhanHang = diaChiNhanHang,
                     HinhThucThanhToan = hinhThucThanhToan, NgayThanhToan = ngayThanhToan)
    db.session.add(hoaDon)
    db.session.commit()
    return hoaDon


def Update(maHoaDon, maKhachHang, diaChiNhanHang, hinhThucThanhToan, ngayThanhToan):
    hoaDon = HoaDons.query.filter(HoaDons.MaHoaDon == maHoaDon).first()
    hoaDon.MaKhachHang = maKhachHang
    hoaDon.DiaChiNhanHang = diaChiNhanHang
    hoaDon.HinhThucThanhToan = hinhThucThanhToan
    hoaDon.NgayThanhToan = ngayThanhToan
    db.session.commit()
    return hoaDon


def Delete(maHoaDon):
    hoaDon = HoaDons.query.filter(HoaDons.MaHoaDon == maHoaDon).first()
    db.session.delete(hoaDon)
    db.session.commit()