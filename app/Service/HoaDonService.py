from app.Repository import HoaDonRepository


def GetHoaDonByMaKhachHang(maKhachHang):
    return HoaDonRepository.GetHoaDonByMaKhachHang(maKhachHang)

def XacNhanHoaDon(maHoaDon):
    HoaDonRepository.XacNhanHoaDon(maHoaDon)

def GetById(maHoaDon):
    return HoaDonRepository.GetById(maHoaDon)