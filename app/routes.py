import os
from app import app, db
from flask import redirect, render_template, flash, url_for
from flask_login import login_user, current_user, logout_user, login_required
from flask import request, jsonify, send_from_directory
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from app.models import SanPhams,  ChiTietSanPhams
from app.Service import SanPhamService, ChiTietSanPhamService, KhachHangService, LoaiSanPhamService, ChiTietHoaDonService, HoaDonService
import json





def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# ===================================================================================================== #
# Sản phẩm:

@app.route('/product', methods=['POST'])
@login_required
def createProduct():
    ProductForm = request.form    
    ProductThumbnail = request.files['thumbnail']
    
    if ProductThumbnail.filename is None:
        flash('No Thumbnail uploaded')        
    elif ProductThumbnail and allowed_file(ProductThumbnail.filename):
        filename = secure_filename(ProductThumbnail.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        ProductThumbnail.save(path)    
    Product = SanPhamService.createSanPham(MaSanPham=ProductForm['MaSanPham'], TenSanPham=ProductForm['TenSanPham']
                                           , Thumbnail=ProductThumbnail.filename, MaLoaiSanPham=ProductForm['MaLoaiSanPham'])
    if Product is None:
        return "Create Product Fail", 500
    return "Create Product Success", 201


@app.route('/product', methods=["GET"])
def getAllProduct():
    ProductList = SanPhamService.getAllSanPham()
    # return jsonify(ProductList) # Lỗi Object of type Product is not JSON serializable

    # Lỗi: Object of type AppenderQuery is not JSON serializable
    #return jsonify(ProductList[0].serialize())

    #Lỗi: Object of type AppenderQuery is not JSON serializable
    list = []
    for product in ProductList:
        list.append(product.serialize())
    return json.dumps(list, indent=4)


@app.route('/product/<int:product_id>/', methods=['GET'])
def getProductByProductId(product_id):
    Product = SanPhamService.getSanPhamById(product_id=product_id)
    return jsonify(Product.serialize())

@app.route('/product/<TenSanPham>/', methods=['GET'])
def getProductByProductName(TenSanPham):
    Product = SanPhamService.getSanPhamByName(TenSanPham)
    return jsonify(Product.serialize())


@app.route('/product/<int:product_id>', methods=['POST'])
@login_required
def updateProductByProductId(product_id):
    ProductForm = request.form
    Action = ProductForm['action']
    if Action == "Update":
        ProductThumbnail = request.files['thumbnail']
        if ProductThumbnail.filename == '':
            flash('No Thumbnail uploaded')
        if ProductThumbnail and allowed_file(ProductThumbnail.filename):
            filename = secure_filename(ProductThumbnail.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            ProductThumbnail.save(path)
        Product = SanPhamService.updateSanPham(MaSanPham=product_id, TenSanPham=ProductForm['TenSanPham'],
                                               Thumbnail=ProductThumbnail.filename,
                                               MaLoaiSanPham=ProductForm['MaLoaiSanPham'])
        if Product is None:
            return "Update product fails", 500
        return "Update product Success", 200
    elif Action == "Delete":
        SanPhamService.deleteSanPham(MaSanPham=product_id)
        return "Delete product Success", 200
    return "No action specified", 400

# ===================================================================================================== #
# Chi tiết sản phẩm:

@app.route('/product-detail/', methods=["GET"])
def getAllProductDetail():
    list = []
    for product in ChiTietSanPhamService.getAllChiTietSanPham():
        list.append(product.serialize())
    return json.dumps(list, indent=4)        


@app.route('/product-detail/<int:product_id>', methods=["get"])
def getAllProductDetailByProductId(product_id):
    ProductDetailList = ChiTietSanPhamService.getAllChiTietSanPhamByProductId(product_id=product_id)
    list = []
    for product in ProductDetailList:
        list.append(product.serialize())
    return json.dumps(list, indent=4)


@app.route("/product-detail/", methods=["POST"])
def createProductDetail():
    DetailProductForm = request.form
    DetailProductAnhLon = request.files['anhLon']
    DetailProductAnhNho = request.files['anhNho']
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
    Detail = ChiTietSanPhamService.createChiTietSanPham(MaChiTietSanPham=DetailProductForm['MaChiTietSanPham'],
                                                        MaSanPham=DetailProductForm['MaSanPham'],
                                                        RAM=DetailProductForm['RAM']
                                                        , ROM=DetailProductForm['ROM'], AnhTo=AnhLonfilename,
                                                        AnhNho=AnhNhofilename
                                                        , Mau=DetailProductForm['Mau'], Gia=DetailProductForm['Gia'],
                                                        SoLuong=DetailProductForm['SoLuong'])
    if Detail is None:
        return "Create Detail Product Fail", 500
    return "Create Detail Product Success", 201


@app.route("/product-detail/<int:product_detail_id>")
def updateProductDetailByProductDetailId(product_detail_id):
    DetailProductForm = request.form
    Action = DetailProductForm['action']
    if Action == "Update":
        DetailProductAnhLon = request.files['anhLon']
        DetailProductAnhNho = request.files['anhNho']
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
                                                            RAM=DetailProductForm['RAM'], ROM=DetailProductForm['ROM'],
                                                            AnhTo=AnhLonfilename, AnhNho=AnhNhofilename,
                                                            Mau=DetailProductForm['Mau'], Gia=DetailProductForm['Gia'],
                                                            SoLuong=DetailProductForm['SoLuong'])
        if Detail is None:
            return "Update product detail fail", 500
        return "Update product detail Success", 200
    elif Action == "Delete":
        ChiTietSanPhamService.deleteChiTietSanPham(MaChiTietSanPham=product_detail_id)
        return "Delete product detail Success", 200
    return "No action specified", 400


@app.route('/product/category/<int:category_id>', methods= ['GET'])
def getProductByCategoryId(category_id):
    Product = SanPhamService.getSanPhambyLoaiId(MaLoaiSanPham=category_id)
    list = []
    for product in Product:
        list.append(product.serialize())
    return json.dumps(list, indent=4)    


# ===================================================================================================== #
# Hóa đơn:
@app.route("/get-hoadonchuathanhtoan", methods=["GET"])
def getHoanDonChuaThanhToan():
    hoaDons = HoaDonService.HienThiHoaDonChuaThanhToan()
    list = []
    for product in hoaDons:
        list.append(product.serialize())
    return json.dumps(list, indent=4)    

@app.route("/get-hoadondathanhtoan", methods=["GET"])
def getHoaDonDaThanhToan():
    hoaDons = HoaDonService.HienThiHoaDonDaThanhToan()
    list = []
    for product in hoaDons:
        list.append(product.serialize())
    return json.dumps(list, indent=4) 


@app.route("/purchase-history/<int:maKhachHang>", methods=["GET"])
@login_required
def GetHoaDonByMaKhachHang(maKhachHang):
    list = []
    for product in HoaDonService.GetHoaDonByMaKhachHang(maKhachHang):
        list.append(product.serialize())
    return json.dumps(list, indent=4)     


@app.route("/xac-nhan/<int:maHoaDon>", methods=["PUT"])
@login_required
def XacNhanHoaDon(maHoaDon):
    return jsonify(HoaDonService.XacNhanHoaDon(maHoaDon).serialize())


@app.route("/get-by-id/<int:maHoaDon>", methods=["GET"])
@login_required
def GetHoaDonById(maHoaDon):
    return jsonify(HoaDonService.GetById(maHoaDon).serialize())


@app.route("/create-hoa-don", methods=["POST"])
@login_required
def CreateHoaDon():
    HoaDonJson = request.get_json()
    HoaDon = HoaDonService.Create(MaKhachHang = HoaDonJson['MaKhachHang'],
                                    DiaChiNhanHang = HoaDonJson['DiaChiNhanHang'],
                                    HinhThucThanhToan = HoaDonJson['HinhThucThanhToan'])
    if HoaDon is None:
        return 'Create Hoa Don Fail',500
    return "Create Hoa Don Success", 201


@app.route("/update-hoa-don", methods=["PUT"])
@login_required
def UpdateHoaDon():
    HoaDonJson = request.form
    HoaDon = HoaDonService.Update(MaKhachHang = HoaDonJson['MaKhachHang'],
                                    DiaChiNhanHang = HoaDonJson['DiaChiNhanHang'],
                                    HinhThucThanhToan = HoaDonJson['HinhThucThanhToan'])
    if HoaDon is None:
        return 'Create Hoa Don Fail',500
    return "Create Hoa Don Success", 201


@app.route("/delete-hoa-don/<int:maHoaDon>", methods=["DELETE"])
@login_required
def Delete(maHoaDon):
    HoaDonService.Delete(maHoaDon)

@app.route("/confirm-payment/<int:maHoaDon>", methods=["PUT"])
def ConfirmPayment(maHoaDon):
    HoaDonService.XacNhanHoaDon(maHoaDon)
    return jsonify(ChiTietHoaDonService.GetByMaHoaDon(maHoaDon).serialize())

# ===================================================================================================== #
# Chi tiết hóa đơn:

@app.route("/detail-purchase-history/<int:maHoaDon>", methods=["GET"])
@login_required
def GetByMaHoaDon(maHoaDon):
    list = []
    for product in ChiTietHoaDonService.GetByMaHoaDon(maHoaDon):
        list.append(product.serialize())
    return json.dumps(list, indent=4)     


@app.route("/create-chi-tiet-hoa-don", methods=["POST"])
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


@app.route("/update-chi-tiet-hoa-don", methods=["PUT"])
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


@app.route("/delete-chi-tiet-hoa-don/<int:maChiTietHoaDon>", methods=["DELETE"])
@login_required
def DeleteChiTietHoaDon(maChiTietHoaDon):
    ChiTietHoaDonService.Delete(maChiTietHoaDon)


@app.route("/tong-tien-da-mua", methods=["GET"])
@login_required
def TongTien():
    return jsonify(ChiTietHoaDonService.TongTien())

# ===================================================================================================== #
# Loại sản phẩm:
@app.route('/category', methods=["GET"])
def getAllCategory():
    CategoryList = LoaiSanPhamService.getAllLoaiSanPham()
    list = []
    for item in CategoryList:
        list.append(item.serialize())
    return json.dumps(list, indent=4)
    

@app.route('/category/<int:MaLoaiSanPham>', methods=["GET"])
def getCategoryById(MaLoaiSanPham):
    Category = LoaiSanPhamService.getLoaiSanPhamById(MaLoaiSanPham)
    return jsonify(Category.serialize())

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
    list = []
    for item in CustomerList:
        list.append(item.serialize())
    return json.dumps(list, indent=4)
    

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

@app.route('/login', methods = ['POST'])
def customerLogin():
    loginInfo = request.get_json()
    username = loginInfo['username']
    password = loginInfo['password']
    KhachHang = KhachHangService.checkLoginKhachHang(username=username, password=password)
    if KhachHang is None:
        return "Wrong Username/Password", 200
    login_user(KhachHang)
    return jsonify(KhachHang.serialize())

@app.route('/logout', methods = ['GET'])
def customerLogout():
    logout_user()
    return "User Logged Out", 200
    
    

