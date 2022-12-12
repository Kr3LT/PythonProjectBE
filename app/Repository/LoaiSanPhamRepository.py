from app.models import LoaiSanPhams
from app import db


def createLoaiSanPham(MaLoaiSanPham, TenLoaiSanPham):
    newLoaiSanPham = LoaiSanPhams(MaLoaiSanPham= MaLoaiSanPham, TenLoaiSanPham= TenLoaiSanPham)
    db.session.add(newLoaiSanPham)
    db.session.commit()
    return newLoaiSanPham

def getAllLoaiSanPham():
    return LoaiSanPhams.query.all()

def updateLoaiSanPham(MaLoaiSanPham, TenLoaiSanPham):
    LoaiSanPham = LoaiSanPhams.query.filter_by(MaLoaiSanPham=MaLoaiSanPham).first_or_404()
    LoaiSanPham.TenLoaiSanPham = TenLoaiSanPham
    db.session.commit()
    return LoaiSanPham

def deleteLoaiSanPham(MaLoaiSanPham):
    LoaiSanPham = LoaiSanPhams.query.filter_by(MaLoaiSanPham=MaLoaiSanPham).first_or_404()
    db.session.delete(LoaiSanPham)
    db.session.commit()
    return "Delete Success"