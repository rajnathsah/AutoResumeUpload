import base64

def encr_passd(password):
    password_bytes = password.encode('ascii')
    base64_bytes = base64.b64encode(password_bytes)
    return base64_bytes.decode('ascii')

def decr_passwd(password):
    base64_bytes = password.encode('ascii')
    password_bytes = base64.b64decode(base64_bytes)
    return password_bytes.decode('ascii')