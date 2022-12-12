from app.models import SanPhams
from app import db


def createSanPham(MaSanPham, TenSanPham, Thumbnail, MaLoaiSanPham):
    newSanpham = SanPhams(MaSanPham=MaSanPham, TenSanPham=TenSanPham
                          , Thumbnail=Thumbnail, MaLoaiSanPham=MaLoaiSanPham)
    db.session.add(newSanpham)
    db.session.commit()
    return newSanpham


def getAllSanPham():
    return SanPhams.query.all()


def getSanPhamById(product_id):
    return SanPhams.query.filter_by(MaSanPham=id).first_or_404()


def updateSanPham(MaSanPham, TenSanPham, Thumbnail, MaLoaiSanPham):
    Product = SanPhams.query.filter_by(MaSanPham=MaSanPham).first_or_404()
    Product.TenSanPham = TenSanPham
    Product.Thumbnail = Thumbnail
    Product.MaLoaiSanPham = MaLoaiSanPham
    db.session.commit()
    return Product


def deleteSanPham(MaSanPham):
    Product = SanPhams.query.filter_by(MaSanPham=MaSanPham).first_or_404()
    db.session.delete(Product)
    db.session.commit()
    return "Delete Success"
