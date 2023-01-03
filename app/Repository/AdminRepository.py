from app.models import Admin
from app import db

def Create(username,password):
    admin = Admin(username=username,password=password)
    db.session.add(admin)
    db.session.commit()
    return admin

def Update(username,password):
    admin = Admin.query.filter(Admin.Username == username).first()
    admin.password = password
    db.session.commit()
    return admin

def Delete(id):
    admin = Admin.get_id(id)
    db.session.delete(admin)
    db.session.commit()
    return "Deleted"

def checkLogin(username, password):
    admin = Admin.query.filter(Admin.Username == username & Admin.Password == password).first()
    if admin is None:
        return None
    return admin
    