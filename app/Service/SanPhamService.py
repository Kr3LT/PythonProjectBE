from app.Repository import SanPhamRepository

def getAllSanPham():
    return SanPhamRepository.getAllSanPham()

def getSanPhambyLoaispId(MaLoaiSanPham):
	return SanPhamRepository.getSanPhambyLoaispId(MaLoaiSanPham=MaLoaiSanPham)

def getSanPhamByName(TenSanPham):
    return SanPhamRepository.getSanPhamByName(TenSanPham = TenSanPham)

def getSanPhamById(product_id):
    return SanPhamRepository.getSanPhamById(product_id = product_id)

def createSanPham(TenSanPham, Thumbnail, MaLoaiSanPham):
    return SanPhamRepository.createSanPham(TenSanPham=TenSanPham, Thumbnail=Thumbnail, MaLoaiSanPham=MaLoaiSanPham)

def updateSanPham(MaSanPham, TenSanPham, Thumbnail, MaLoaiSanPham):
    return SanPhamRepository.updateSanPham(MaSanPham=MaSanPham, TenSanPham=TenSanPham, Thumbnail=Thumbnail, MaLoaiSanPham=MaLoaiSanPham)


def deleteSanPham(MaSanPham):
    return SanPhamRepository.deleteSanPham(MaSanPham=MaSanPham)