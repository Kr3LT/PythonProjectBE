from app.Repository import KhachHangRepository

def createKhachHang(MaKhachHang, TenKhachHang, SoDienThoai, DiaChi, UserName, Password):
    return KhachHangRepository.createKhachHang(MaKhachHang=MaKhachHang, TenKhachHang=TenKhachHang, SoDienThoai=SoDienThoai, DiaChi=DiaChi, UserName=UserName, Password=Password)

def getAllKhachHang():
    return KhachHangRepository.getAllKhachHang()

def updateKhachHang(MaKhachHang, TenKhachHang, SoDienThoai, DiaChi, Password):
    return KhachHangRepository.updateKhachHang(MaKhachHang, TenKhachHang, SoDienThoai, DiaChi, Password)

def deleteKhachHang(MaKhachHang):
    return KhachHangRepository.deleteKhachHang(MaKhachHang)

def checkLoginKhachHang(username, password):
    return KhachHangRepository.checkLoginKhachHang(username=username, password=password)