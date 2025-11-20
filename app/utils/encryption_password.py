import bcrypt

def encrypt_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(hashed, password):
    return bcrypt.checkpw(password.encode(), hashed.encode())
