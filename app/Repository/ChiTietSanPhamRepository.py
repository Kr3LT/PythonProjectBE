from app.models import ChiTietSanPhams
from app import db

def getAllChiTietSanPham():
    return ChiTietSanPhams.query.all()

def getAllChiTietSanPhamByProductId(product_id):
    return ChiTietSanPhams.query.filter_by(MaSanPham = product_id).all()

def getAllChiTietSanPhamByPrice(min,max):
    return ChiTietSanPhams.query.filter(ChiTietSanPhams.Gia.between(min,max)).all()

def getAllChiTietSanPhamByConfiguration(RAM,ROM,Mau):
    return ChiTietSanPhams.query.filter(ChiTietSanPhams.RAM.like('%'+RAM+'%')  & ChiTietSanPhams.ROM.like('%'+ROM+'%') & ChiTietSanPhams.Mau.like('%'+Mau+'%')).all()

def createChiTietSanPham(MaChiTietSanPham,MaSanPham, RAM, ROM, AnhTo, AnhNho
                        , Mau, Gia, SoLuong):
    newChiTietSanPham = ChiTietSanPhams(MaChiTietSanPham=MaChiTietSanPham,MaSanPham=MaSanPham, RAM=RAM
                                        , ROM=ROM, AnhTo=AnhTo, AnhNho=AnhNho
                                        , Mau=Mau, Gia=Gia,SoLuong=SoLuong)
    db.session.add(newChiTietSanPham)
    db.session.commit()
    return newChiTietSanPham
def updateChiTietSanPham(MaChiTietSanPham, RAM, ROM, AnhTo, AnhNho
                        , Mau, Gia, SoLuong):
    ProductDetail = ChiTietSanPhams.query.filter_by(MaChiTietSanPham=MaChiTietSanPham).first_or_404()
    ProductDetail.RAM = RAM
    ProductDetail.ROM = ROM
    ProductDetail.AnhTo = AnhTo
    ProductDetail.AnhNho = AnhNho
    ProductDetail.Mau = Mau
    ProductDetail.Gia = Gia
    ProductDetail.SoLuong = SoLuong
    db.session.commit()
    return ProductDetail
def deleteChiTietSanPham(MaChiTietSanPham):
    ProductDetail = ChiTietSanPhams.query.filter_by(MaChiTietSanPham=MaChiTietSanPham).first_or_404()
    db.session.delete(ProductDetail)
    return "Delete Success"

