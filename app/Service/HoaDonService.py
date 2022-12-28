from app.Repository import HoaDonRepository

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
    HoaDonRepository.Delete(maHoaDon)