import os
from app import app,db
from flask import redirect, render_template,flash, url_for
from flask_login import login_user, current_user, logout_user, login_required
from flask import request, jsonify,send_from_directory
from werkzeug.urls import url_parse 
from werkzeug.utils import secure_filename
from app.models import SanPhams,LoaiSanPhams, ChiTietSanPhams
from app.Service import SanPhamService,ChiTietSanPhamService

def allowed_file(filename): 
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS'] 

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename) 


@app.route('/product', methods = ['POST'])
@login_required
def createProduct():
    ProductJson = request.get_json()
    ProductThumbnail = request.file['thumbnail']
    if ProductThumbnail.filename == '':
        flash('No Thumbnail uploaded')
    if ProductThumbnail and allowed_file(ProductThumbnail.filename):
        filename = secure_filename(ProductThumbnail.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        ProductThumbnail.save(path)
    Product = SanPhamService.createSanPham(MaSanPham=ProductJson['MaSanPham'],TenSanPham=ProductJson['TenSanPham']
                          ,Thumbnail = filename, MaLoaiSanPham = ProductJson['MaLoaiSanPham'])
    if Product is None:
        return "Create Product Fail", 500
    return "Create Product Success", 201

@app.route('/product', methods=["GET"])
def getAllProduct():
    ProductList = SanPhamService.getAllSanPham()
    return jsonify(ProductList)
    
@app.route('/product/<int:product_id>/', methods = ['GET'])
def getProductByProductId(product_id):    
    Product = SanPhamService.getSanPhamById(product_id=product_id)
    return jsonify(Product)
    
@app.route('/product/<int:product_id>', methods = ['POST'])
@login_required
def updateProductByProductId(product_id):
    ProductJson = request.get_json()
    Action = ProductJson['action']
    if Action == "Update":
        ProductThumbnail = request.file['thumbnail']
        if ProductThumbnail.filename == '':
            flash('No Thumbnail uploaded')
        if ProductThumbnail and allowed_file(ProductThumbnail.filename):
            filename = secure_filename(ProductThumbnail.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            ProductThumbnail.save(path)
        Product = SanPhamService.updateSanPham(MaSanPham=product_id,TenSanPham=ProductJson['TenSanPham'],
                                     Thumbnail=ProductThumbnail.filename,MaLoaiSanPham=ProductJson['MaLoaiSanPham'])
        if Product is None:
            return "Update product fails", 500
        return "Update product Success", 200
    elif Action == "Delete":
        SanPhamService.deleteSanPham(MaSanPham=product_id)
        return "Delete product Success",200
    return "No action specified",400

@app.route('/product-detail/', methods = ["GET"])
def getAllProductDetail():
    return jsonify(ChiTietSanPhamService.getAllChiTietSanPham())

@app.route('/product-detail/<int:product_id>', methods = ["get"])
def getAllProductDetailByProductId(product_id):
    ProductDetailList = ChiTietSanPhamService.getAllChiTietSanPhamByProductId(product_id=product_id)
    return jsonify(ProductDetailList)

@app.route("/product-detail/", methods = ["POST"])
def createProductDetail():
    DetailProductJson = request.get_json()
    DetailProductAnhLon = request.file['anhLon']
    DetailProductAnhNho = request.file['anhNho']
    if DetailProductAnhLon.filename == '' or DetailProductAnhNho.filename == '':
        flash('No Thumbnail uploaded')
    if DetailProductAnhLon and allowed_file(DetailProductAnhLon.filename) and DetailProductAnhNho and allowed_file(DetailProductAnhNho.filename):
        AnhLonfilename = secure_filename(DetailProductAnhLon.filename)
        AnhLonpath = os.path.join(app.config['UPLOAD_FOLDER'], AnhLonfilename)
        DetailProductAnhLon.save(AnhLonpath)
        AnhNhofilename= secure_filename(DetailProductAnhNho.filename)
        AnhNhopath = os.path.join(app.config['UPLOAD_FOLDER'], AnhNhofilename)
        DetailProductAnhNho.save(AnhNhopath)
    Detail = ChiTietSanPhamService.createChiTietSanPham(MaChiTietSanPham = DetailProductJson['MaChiTietSanPham'],MaSanPham = DetailProductJson['MaSanPham'], RAM = DetailProductJson['RAM']
                                        , ROM = DetailProductJson['ROM'], AnhTo = AnhLonfilename, AnhNho = AnhNhofilename
                                        ,Mau = DetailProductJson['Mau'], Gia = DetailProductJson['Gia'],SoLuong = DetailProductJson['SoLuong'])
    if Detail is None:
        return "Create Detail Product Fail",500
    return "Create Detail Product Success", 201

@app.route("/product-detail/<int:product_detail_id")
def updateProductDetailByProductDetailId(product_detail_id):
    DetailProductJson = request.get_json()
    Action = DetailProductJson['action']
    if Action == "Update":
        DetailProductAnhLon = request.file['anhLon']
        DetailProductAnhNho = request.file['anhNho']
        if DetailProductAnhLon.filename == '' or DetailProductAnhNho.filename == '':
            flash('No Thumbnail uploaded')
        if DetailProductAnhLon and allowed_file(DetailProductAnhLon.filename) and DetailProductAnhNho and allowed_file(DetailProductAnhNho.filename):
            AnhLonfilename = secure_filename(DetailProductAnhLon.filename)
            AnhLonpath = os.path.join(app.config['UPLOAD_FOLDER'], AnhLonfilename)
            DetailProductAnhLon.save(AnhLonpath)
            AnhNhofilename= secure_filename(DetailProductAnhNho.filename)
            AnhNhopath = os.path.join(app.config['UPLOAD_FOLDER'], AnhNhofilename)
            DetailProductAnhNho.save(AnhNhopath)
        Detail = ChiTietSanPhamService.updateChiTietSanPham(MaChiTietSanPham=product_detail_id,
                                                   RAM=DetailProductJson['RAM'],ROM=DetailProductJson['ROM'],
                                                   AnhTo=AnhLonfilename,AnhNho=AnhNhofilename,
                                                   Mau=DetailProductJson['Mau'],Gia=DetailProductJson['Gia'],
                                                   SoLuong=DetailProductJson['SoLuong'])
        if Detail is None:
            return "Update product detail fail",500
        return "Update product detail Success", 200
    elif Action == "Delete":
        ChiTietSanPhamService.deleteChiTietSanPham(MaChiTietSanPham=product_detail_id)
        return "Delete product detail Success",200
    return "No action specified",400

