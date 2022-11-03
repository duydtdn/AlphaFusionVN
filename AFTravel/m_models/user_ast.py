from AFTravel.m_models.ModelField import ModelField

def get_password_field():

    password = ModelField()
    password.name = 'password'
    password.mean = 'password'
    password.mode = 'Password'
    return password

def get_password_hash_field():
    password_hash = ModelField()
    password_hash.name = 'password_hash'
    password_hash.mean = 'password_hash'
    password_hash.mode = 'Text'
    return password_hash

def get_password_salt_field():
    password_salt = ModelField()
    password_salt.name = 'password_salt'
    password_salt.mean = 'password_salt'
    password_salt.mode = 'Text'
    return password_salt

def get_status_field():
    status = ModelField()
    status.name = 'status'
    status.mean = 'status'
    status.mode = 'Text'
    return status

def get_email_field():
    email = ModelField()
    email.name = 'email'
    email.mean = 'email'
    email.mode = 'Text'
    return email

def get_username_field():
    username = ModelField()
    username.name = 'username'
    username.mean = 'Ten dang nhap'
    username.mode = 'Text'
    return username

def get_fields():
    name = ModelField()
    name.name = 'name'
    name.mean = 'Tên của bạn'
    name.mode = 'Text'


    username = get_username_field()
    password = get_password_field()
    email = get_email_field()
    return [name, username, email, password]
