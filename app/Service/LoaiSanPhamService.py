from app.Repository import LoaiSanPhamRepository

def createLoaiSanPham(MaLoaiSanPham, TenLoaiSanPham):
    return LoaiSanPhamRepository.createLoaiSanPham(MaLoaiSanPham, TenLoaiSanPham)

def getAllLoaiSanPham():
    return LoaiSanPhamRepository.getAllLoaiSanPham()

def getLoaiSanPhamById(MaLoaiSanPham):
    return LoaiSanPhamRepository.getLoaiSanPhamById(MaLoaiSanPham)
    
def updateLoaiSanPham(MaLoaiSanPham, TenLoaiSanPham):
    return LoaiSanPhamRepository.updateLoaiSanPham(MaLoaiSanPham, TenLoaiSanPham)

def deleteLoaiSanPham(MaLoaiSanPham):
    return LoaiSanPhamRepository.deleteLoaiSanPham(MaLoaiSanPham)