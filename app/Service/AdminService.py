from app.Repository import AdminRepository


def Create(username,password):    
    return AdminRepository.Create(username,password)

def Update(username,password):    
    return AdminRepository.Update(username,password)

def Delete(id):
    return AdminRepository.Delete(id)

def checkLogin(username, password):
    return AdminRepository.checkLogin(username,password)