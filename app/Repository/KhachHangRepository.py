from app.models import KhachHangs
from app import db

def createKhachHang(MaKhachHang, TenKhachHang, SoDienThoai, DiaChi, UserName, Password):
    newKhachHang = KhachHangs(MaKhachHang= MaKhachHang, TenKhachHang= TenKhachHang, 
                              SoDienThoai = SoDienThoai, DiaChi = DiaChi, Username = UserName, Password = Password)
    db.session.add(newKhachHang)
    db.session.commit()
    return newKhachHang

def getAllKhachHang():
    return KhachHangs.query.all()

def updateKhachHang(MaKhachHang, TenKhachHang, SoDienThoai, DiaChi, Password):
    KhachHang = KhachHangs.query.filter_by(MaKhachHang=MaKhachHang).first_or_404()
    KhachHang.TenKhachHang = TenKhachHang
    KhachHang.SoDienThoai = SoDienThoai
    KhachHang.DiaChi = DiaChi
    KhachHang.Password = Password
    db.session.commit()
    return KhachHang

def deleteKhachHang(MaKhachHang):
    KhachHang = KhachHangs.query.filter_by(MaKhachHang=MaKhachHang).first_or_404()
    db.session.delete(KhachHang)
    db.session.commit()
    return "Delete Success"

def checkLoginKhachHang(username, password):
    KhachHang = KhachHangs.query.filter_by(Username = username, Password = password).first_or_404()
    return KhachHang