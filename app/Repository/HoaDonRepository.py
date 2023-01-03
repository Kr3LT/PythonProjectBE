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

def HienThiHoaDonChuaThanhToan():
    hoadons = HoaDons.query.filter(HoaDons.NgayThanhToan==None).all()
    return hoadons
def HienThiHoaDonDaThanhToan():
    hoadons = HoaDons.query.filter(HoaDons.NgayThanhToan!= None).all()
    return hoadons

def GetById(maHoaDon):
    return HoaDons.query.filter(HoaDons.MaHoaDon == maHoaDon).first()


def Create(maKhachHang, diaChiNhanHang, hinhThucThanhToan):
    hoaDon = HoaDons(MaKhachHang = maKhachHang, DiaChiNhanHang = diaChiNhanHang,
                     HinhThucThanhToan = hinhThucThanhToan)
    db.session.add(hoaDon)
    db.session.commit()
    return hoaDon


def Update(maHoaDon, maKhachHang, diaChiNhanHang, hinhThucThanhToan):
    hoaDon = HoaDons.query.filter(HoaDons.MaHoaDon == maHoaDon).first()
    hoaDon.MaKhachHang = maKhachHang
    hoaDon.DiaChiNhanHang = diaChiNhanHang
    hoaDon.HinhThucThanhToan = hinhThucThanhToan
    db.session.commit()
    return hoaDon


def Delete(maHoaDon):
    hoaDon = HoaDons.query.filter(HoaDons.MaHoaDon == maHoaDon).first()
    db.session.delete(hoaDon)
    db.session.commit()
    return "Deleted"

    