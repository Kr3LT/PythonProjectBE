from app.Repository import ChiTietHoaDonRepository


def GetByMaHoaDon(maHoaDon):
    return ChiTietHoaDonRepository.GetByMaHoaDon(maHoaDon)