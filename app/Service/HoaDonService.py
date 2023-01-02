from app.Repository import HoaDonRepository, ChiTietHoaDonRepository

def HienThiHoaDonChuaThanhToan():
    return HoaDonRepository.HienThiHoaDonChuaThanhToan()

def HienThiHoaDonDaThanhToan():
    return HoaDonRepository.HienThiHoaDonDaThanhToan()

def GetHoaDonByMaKhachHang(maKhachHang):
    return HoaDonRepository.GetHoaDonByMaKhachHang(maKhachHang)


def XacNhanHoaDon(maHoaDon):
    return HoaDonRepository.XacNhanHoaDon(maHoaDon)


def GetById(maHoaDon):
    return HoaDonRepository.GetById(maHoaDon)


def Create(maKhachHang, diaChiNhanHang, hinhThucThanhToan, ngayThanhToan):
    return HoaDonRepository.Create(maKhachHang, diaChiNhanHang, hinhThucThanhToan, ngayThanhToan)


def Update(maHoaDon, maKhachHang, diaChiNhanHang, hinhThucThanhToan, ngayThanhToan):
    return HoaDonRepository.Update(maHoaDon, maKhachHang, diaChiNhanHang, hinhThucThanhToan, ngayThanhToan)


def Delete(maHoaDon):
    return HoaDonRepository.Delete(maHoaDon)

def TongTienDaMua(maKhachHang):
    HoaDonList = HoaDonRepository.GetHoaDonByMaKhachHang(maKhachHang=maKhachHang)
    TongTien = 0
    for HoaDon in HoaDonList :
        TongTien += ChiTietHoaDonRepository.TongTien(HoaDon.MaHoaDon)    
    return TongTien