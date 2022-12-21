import os
from app import app, db
from flask import redirect, render_template, flash, url_for
from flask_login import login_user, current_user, logout_user, login_required
from flask import request, jsonify, send_from_directory
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from app.models import SanPhams,  ChiTietSanPhams
from app.Service import SanPhamService, ChiTietSanPhamService, KhachHangService, LoaiSanPhamService, ChiTietHoaDonService, HoaDonService


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/product', methods=['POST'])
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
    Product = SanPhamService.createSanPham(MaSanPham=ProductJson['MaSanPham'], TenSanPham=ProductJson['TenSanPham']
                                           , Thumbnail=filename, MaLoaiSanPham=ProductJson['MaLoaiSanPham'])
    if Product is None:
        return "Create Product Fail", 500
    return "Create Product Success", 201


@app.route('/product', methods=["GET"])
def getAllProduct():
    ProductList = SanPhamService.getAllSanPham()
    return jsonify(ProductList)


@app.route('/product/<int:product_id>/', methods=['GET'])
def getProductByProductId(product_id):
    Product = SanPhamService.getSanPhamById(product_id=product_id)
    return jsonify(Product)


@app.route('/product/<int:product_id>', methods=['POST'])
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
        Product = SanPhamService.updateSanPham(MaSanPham=product_id, TenSanPham=ProductJson['TenSanPham'],
                                               Thumbnail=ProductThumbnail.filename,
                                               MaLoaiSanPham=ProductJson['MaLoaiSanPham'])
        if Product is None:
            return "Update product fails", 500
        return "Update product Success", 200
    elif Action == "Delete":
        SanPhamService.deleteSanPham(MaSanPham=product_id)
        return "Delete product Success", 200
    return "No action specified", 400


@app.route('/product-detail/', methods=["GET"])
def getAllProductDetail():
    return jsonify(ChiTietSanPhamService.getAllChiTietSanPham())


@app.route('/product-detail/<int:product_id>', methods=["get"])
def getAllProductDetailByProductId(product_id):
    ProductDetailList = ChiTietSanPhamService.getAllChiTietSanPhamByProductId(product_id=product_id)
    return jsonify(ProductDetailList)


@app.route("/product-detail/", methods=["POST"])
def createProductDetail():
    DetailProductJson = request.get_json()
    DetailProductAnhLon = request.file['anhLon']
    DetailProductAnhNho = request.file['anhNho']
    if DetailProductAnhLon.filename == '' or DetailProductAnhNho.filename == '':
        flash('No Thumbnail uploaded')
    if DetailProductAnhLon and allowed_file(DetailProductAnhLon.filename) and DetailProductAnhNho and allowed_file(
            DetailProductAnhNho.filename):
        AnhLonfilename = secure_filename(DetailProductAnhLon.filename)
        AnhLonpath = os.path.join(app.config['UPLOAD_FOLDER'], AnhLonfilename)
        DetailProductAnhLon.save(AnhLonpath)
        AnhNhofilename = secure_filename(DetailProductAnhNho.filename)
        AnhNhopath = os.path.join(app.config['UPLOAD_FOLDER'], AnhNhofilename)
        DetailProductAnhNho.save(AnhNhopath)
    Detail = ChiTietSanPhamService.createChiTietSanPham(MaChiTietSanPham=DetailProductJson['MaChiTietSanPham'],
                                                        MaSanPham=DetailProductJson['MaSanPham'],
                                                        RAM=DetailProductJson['RAM']
                                                        , ROM=DetailProductJson['ROM'], AnhTo=AnhLonfilename,
                                                        AnhNho=AnhNhofilename
                                                        , Mau=DetailProductJson['Mau'], Gia=DetailProductJson['Gia'],
                                                        SoLuong=DetailProductJson['SoLuong'])
    if Detail is None:
        return "Create Detail Product Fail", 500
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
        if DetailProductAnhLon and allowed_file(DetailProductAnhLon.filename) and DetailProductAnhNho and allowed_file(
                DetailProductAnhNho.filename):
            AnhLonfilename = secure_filename(DetailProductAnhLon.filename)
            AnhLonpath = os.path.join(app.config['UPLOAD_FOLDER'], AnhLonfilename)
            DetailProductAnhLon.save(AnhLonpath)
            AnhNhofilename = secure_filename(DetailProductAnhNho.filename)
            AnhNhopath = os.path.join(app.config['UPLOAD_FOLDER'], AnhNhofilename)
            DetailProductAnhNho.save(AnhNhopath)
        Detail = ChiTietSanPhamService.updateChiTietSanPham(MaChiTietSanPham=product_detail_id,
                                                            RAM=DetailProductJson['RAM'], ROM=DetailProductJson['ROM'],
                                                            AnhTo=AnhLonfilename, AnhNho=AnhNhofilename,
                                                            Mau=DetailProductJson['Mau'], Gia=DetailProductJson['Gia'],
                                                            SoLuong=DetailProductJson['SoLuong'])
        if Detail is None:
            return "Update product detail fail", 500
        return "Update product detail Success", 200
    elif Action == "Delete":
        ChiTietSanPhamService.deleteChiTietSanPham(MaChiTietSanPham=product_detail_id)
        return "Delete product detail Success", 200
    return "No action specified", 400

# ===================================================================================================== #
# Hóa đơn:

@app.route("purchase-history/<int:maKhachHang>", method=["GET"])
@login_required
def GetHoaDonByMaKhachHang(maKhachHang):
    return jsonify(HoaDonService.GetHoaDonByMaKhachHang(maKhachHang))


@app.route("xac-nhan/<int:maHoaDon>", method=["PUT"])
@login_required
def XacNhanHoaDon(maHoaDon):
    return jsonify(HoaDonService.XacNhanHoaDon(maHoaDon))


@app.route("get-by-id/<int:maHoaDon>", method=["GET"])
@login_required
def GetHoaDonById(maHoaDon):
    return jsonify(HoaDonService.GetById(maHoaDon))


@app.route("create-hoa-don", method=["POST"])
@login_required
def CreateHoaDon():
    HoaDonJson = request.get_json()
    HoaDon = HoaDonService.Create(MaKhachHang = HoaDonJson['MaKhachHang'],
                                    DiaChiNhanHang = HoaDonJson['DiaChiNhanHang'],
                                    HinhThucThanhToan = HoaDonJson['HinhThucThanhToan'])
    if HoaDon is None:
        return 'Create Hoa Don Fail',500
    return "Create Hoa Don Success", 201


@app.route("update-hoa-don", method=["PUT"])
@login_required
def UpdateHoaDon():
    HoaDonJson = request.get_json()
    HoaDon = HoaDonService.Update(MaKhachHang = HoaDonJson['MaKhachHang'],
                                    DiaChiNhanHang = HoaDonJson['DiaChiNhanHang'],
                                    HinhThucThanhToan = HoaDonJson['HinhThucThanhToan'])
    if HoaDon is None:
        return 'Create Hoa Don Fail',500
    return "Create Hoa Don Success", 201


@app.route("delete-hoa-don/<int: maHoaDon>", method=["DELETE"])
@login_required
def Delete(maHoaDon):
    HoaDonService.Delete(maHoaDon)

# ===================================================================================================== #
# Chi tiết hóa đơn:

@app.route("detail-purchase-history/<int:maHoaDon>", method=["GET"])
@login_required
def GetByMaHoaDon(maHoaDon):
    return jsonify(ChiTietHoaDonService.GetByMaHoaDon(maHoaDon))


@app.route("create-chi-tiet-hoa-don", method=["POST"])
@login_required
def CreateChiTietHoaDon():
    ChiTietHoaDonJson = request.get_json()
    ChiTietHoaDon = ChiTietHoaDonService.Create(MaHoaDon = ChiTietHoaDonJson['MaHoaDon'],
                                                MaSanPham = ChiTietHoaDonJson['MaSanPham'],
                                                SoLuong = ChiTietHoaDonJson['ChiTietHoaDonJson'],
                                                DonGia = ChiTietHoaDonJson['ChiTietHoaDonJson'])
    if ChiTietHoaDon is None:
        return 'Create Chi Tiet Hoa Don Fail',500
    return "Create Chi Tiet Hoa Don Success", 201


@app.route("update-chi-tiet-hoa-don", method=["PUT"])
@login_required
def UpdateChiTietHoaDon():
    ChiTietHoaDonJson = request.get_json()
    ChiTietHoaDon = ChiTietHoaDonService.Update(MaChiTietHoaDon = ChiTietHoaDonJson['MaChiTietHoaDon'],
                                                MaHoaDon = ChiTietHoaDonJson['MaHoaDon'],
                                                MaSanPham = ChiTietHoaDonJson['MaSanPham'],
                                                SoLuong = ChiTietHoaDonJson['ChiTietHoaDonJson'],
                                                DonGia = ChiTietHoaDonJson['ChiTietHoaDonJson'])
    if ChiTietHoaDon is None:
        return 'Create Chi Tiet Hoa Don Fail',500
    return "Create Chi Tiet Hoa Don Success", 201


@app.route("delete-chi-tiet-hoa-don/<int: maChiTietHoaDon>", method=["DELETE"])
@login_required
def DeleteChiTietHoaDon(maChiTietHoaDon):
    ChiTietHoaDonService.Delete(maChiTietHoaDon)


@app.route("tong-tien-da-mua/<int: maChiTietHoaDon>", method=["GET"])
@login_required
def TongTien():
    return jsonify(ChiTietHoaDonService.TongTien())

# ===================================================================================================== #
# Loại sản phẩm:
@app.route('/category', methods=["GET"])
def getAllCategory():
    CategoryList = LoaiSanPhamService.getAllLoaiSanPham()
    return jsonify(CategoryList)

@app.route('/category', methods = ['POST'])
@login_required
def createCategory():
    CategoryJson = request.get_json()
    Category = LoaiSanPhamService.createLoaiSanPham(MaLoaiSanPham= CategoryJson['MaLoaiSanPham'],
                                                    TenLoaiSanPham= CategoryJson['TenLoaiSanPham'])
    if Category is None:
        return "Create Category Fail",500
    return "Create Category Success", 201

@app.route('/category/<int:MaLoaiSanPham>', methods = ['POST'])
@login_required
def updateCategoryByCategoryId(MaLoaiSanPham):
    CategoryJson = request.get_json()
    Action = CategoryJson['action']
    if Action == "Update":
        Category = LoaiSanPhamService.updateLoaiSanPham(MaLoaiSanPham = MaLoaiSanPham, TenLoaiSanPham = CategoryJson['TenLoaiSanPham'])
        if Category is None:
            return "Update Category detail fail",500
        return "Update Category Success", 200
    elif Action == "Delete":
        LoaiSanPhamService.deleteLoaiSanPham(MaLoaiSanPham = MaLoaiSanPham)
        return "Delete Category Success",200
    return "No action specified",400

# ===================================================================================================== #
# Khách hàng:
@app.route('/customer', methods=["GET"])
def getAllCustomer():
    CustomerList = KhachHangService.getAllKhachHang()
    return jsonify(CustomerList)

@app.route('/customer', methods = ['POST'])
def createCustomer():
    CustomerJson = request.get_json()
    Customer = KhachHangService.createKhachHang(MaKhachHang = CustomerJson['MaKhachHang'], TenKhachHang = CustomerJson['TenKhachHang'],
                              SoDienThoai = CustomerJson['SoDienThoai'], DiaChi = CustomerJson['DiaChi'])   
    if Customer is None:
        return "Create Customer Fail",500
    return "Create Customer Success", 201

@app.route('/customer/<int:MaKhachHang>', methods = ['POST'])
@login_required
def updateCustomerByCustomerId(MaKhachHang):
    CustomerJson = request.get_json()
    Action = CustomerJson['action']
    if Action == "Update":
        Customer = KhachHangService.updateKhachHang(MaKhachHang = MaKhachHang, TenKhachHang = CustomerJson['TenKhachHang'],
                              SoDienThoai = CustomerJson['SoDienThoai'], DiaChi = CustomerJson['DiaChi'])
        if Customer is None:
            return "Update Customer detail fail",500
        return "Update Customer Success", 200
    elif Action == "Delete":
        LoaiSanPhamService.deleteLoaiSanPham(MaKhachHang = MaKhachHang)
        return "Delete Customer Success",200
    return "No action specified",400
@app.route("confirm-payment/<int:ma-hoa-don>", method=["PUT"])
def XacNhanHoaDon(maHoaDon):
    HoaDonService.XacNhanHoaDon(maHoaDon)
    return jsonify(ChiTietHoaDonService.GetByMaHoaDon(maHoaDon))