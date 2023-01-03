from app.Repository import ChiTietHoaDonRepository


def GetAll():
    return ChiTietHoaDonRepository.GetAll()


def GetByMaHoaDon(maHoaDon):
    return ChiTietHoaDonRepository.GetByMaHoaDon(maHoaDon)


def Create(maHoaDon, maChiTietSanPham, soLuong, donGia):
    return ChiTietHoaDonRepository.Create(maHoaDon, maChiTietSanPham, soLuong, donGia)


def Update(maChiTietHoaDon, maHoaDon, maChiTietSanPham, soLuong, donGia):
    return ChiTietHoaDonRepository.Update(maChiTietHoaDon, maHoaDon, maChiTietSanPham, soLuong, donGia)


def Delete(maChiTietHoaDon):
    return ChiTietHoaDonRepository.Delete(maChiTietHoaDon)


def TongTien(maHoaDon):
    return ChiTietHoaDonRepository.TongTien(maHoaDon)
