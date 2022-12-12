from app.Repository import LoaiSanPhamRepository

def createLoaiSanPham(MaLoaiSanPham, TenLoaiSanPham):
    return LoaiSanPhamRepository.createLoaiSanPham(MaLoaiSanPham, TenLoaiSanPham)

def getAllLoaiSanPham():
    return LoaiSanPhamRepository.getAllLoaiSanPham()
    
def updateLoaiSanPham(MaLoaiSanPham, TenLoaiSanPham):
    return LoaiSanPhamRepository.updateLoaiSanPham(MaLoaiSanPham, TenLoaiSanPham)

def deleteLoaiSanPham(MaLoaiSanPham):
    return LoaiSanPhamRepository.deleteLoaiSanPham(MaLoaiSanPham)