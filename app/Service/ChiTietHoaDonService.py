from app.Repository import ChiTietHoaDonRepository


def GetByMaHoaDon(maHoaDon):
    return ChiTietHoaDonRepository.GetByMaHoaDon(maHoaDon)


def Create(maHoaDon, maSanPham, soLuong, donGia):
    return ChiTietHoaDonRepository.Create(maHoaDon, maSanPham, soLuong, donGia)


def Update(maChiTietHoaDon, maHoaDon, maSanPham, soLuong, donGia):
    return ChiTietHoaDonRepository.Update(maChiTietHoaDon, maHoaDon, maSanPham, soLuong, donGia)


def Delete(maChiTietHoaDon):
    ChiTietHoaDonRepository.Delete(maChiTietHoaDon)


def TongTien():
    return ChiTietHoaDonRepository.TongTien()