from app.Repository import KhachHangRepository

def createKhachHang(MaKhachHang, TenKhachHang, SoDienThoai, DiaChi):
    return KhachHangRepository.createKhachHang(MaKhachHang, TenKhachHang, SoDienThoai, DiaChi)

def getAllKhachHang():
    return KhachHangRepository.getAllKhachHang()

def updateKhachHang(MaKhachHang, TenKhachHang, SoDienThoai, DiaChi):
    return KhachHangRepository.updateKhachHang(MaKhachHang, TenKhachHang, SoDienThoai, DiaChi)

def deleteKhachHang(MaKhachHang):
    return KhachHangRepository.deleteKhachHang(MaKhachHang)

def checkLoginKhachHang(username, password):
    return KhachHangRepository.checkLoginKhachHang(username=username, password=password)