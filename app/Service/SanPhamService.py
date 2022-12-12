from app.Repository import SanPhamRepository

def getAllSanPham():
    return SanPhamRepository.getAllSanPham()


def getSanPhamById(product_id):
    return SanPhamRepository.getSanPhamById(product_id = product_id)

def createSanPham(MaSanPham, TenSanPham, Thumbnail, MaLoaiSanPham):
    return SanPhamRepository.createSanPham(MaSanPham=MaSanPham, TenSanPham=TenSanPham, Thumbnail=Thumbnail, MaLoaiSanPham=MaLoaiSanPham)

def updateSanPham(MaSanPham, TenSanPham, Thumbnail, MaLoaiSanPham):
    return SanPhamRepository.updateSanPham(MaSanPham=MaSanPham, TenSanPham=TenSanPham, Thumbnail=Thumbnail, MaLoaiSanPham=MaLoaiSanPham)


def deleteSanPham(MaSanPham):
    return SanPhamRepository.deleteSanPham(MaSanPham=MaSanPham)