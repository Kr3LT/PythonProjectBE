from app.Repository import ChiTietSanPhamRepository


def getAllChiTietSanPham():
    return ChiTietSanPhamRepository.getAllChiTietSanPham()

def getAllChiTietSanPhamByProductId(product_id):
    return ChiTietSanPhamRepository.getAllChiTietSanPhamByProductId(product_id=product_id)

def getAllChiTietSanPhamByPrice(min,max):
    return ChiTietSanPhamRepository.getAllChiTietSanPhamByPrice(min=min,max=max)

def getAllChiTietSanPhamByByConfiguration(RAM,ROM,Mau):
    return ChiTietSanPhamRepository.getAllChiTietSanPhamByConfiguration(RAM=RAM,ROM=ROM,Mau=Mau)

def createChiTietSanPham(MaChiTietSanPham, MaSanPham, RAM, ROM, AnhTo, AnhNho
                         , Mau, Gia, SoLuong):
    return ChiTietSanPhamRepository.createChiTietSanPham(MaChiTietSanPham=MaChiTietSanPham, MaSanPham=MaSanPham,
                                                         RAM=RAM, ROM=ROM, AnhTo=AnhTo, AnhNho=AnhNho
                                                         , Mau=Mau, Gia=Gia, SoLuong=SoLuong)

def updateChiTietSanPham(MaChiTietSanPham, RAM, ROM, AnhTo, AnhNho
                         , Mau, Gia, SoLuong):
    return ChiTietSanPhamRepository.updateChiTietSanPham(MaChiTietSanPham=MaChiTietSanPham, RAM=RAM, ROM=ROM,
                                                         AnhTo=AnhTo, AnhNho=AnhNho
                                                         , Mau=Mau, Gia=Gia, SoLuong=SoLuong)


def deleteChiTietSanPham(MaChiTietSanPham):
    return ChiTietSanPhamRepository.deleteChiTietSanPham(MaChiTietSanPham=MaChiTietSanPham)
