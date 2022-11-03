from AFTravel.m_models.ModelField import ModelField


def get_m_id_field():
    m_id = ModelField()
    m_id.name = 'm_id'
    m_id.mean = 'm_id'
    m_id.mode = 'text'
    return m_id


def get_name_field():
    name = ModelField()
    name.name = 'name'
    name.mean = 'Tên'
    name.mode = 'text'
    return name


def get_address_field():
    address = ModelField()
    address.name = 'address'
    address.mean = 'Địa chỉ'
    address.mode = 'text'
    return address


def get_avatar_field():
    avatar = ModelField()
    avatar.name = 'avatar'
    avatar.mean = 'Hình đại diện'
    avatar.mode = 'text'
    return avatar


def get_basic_price_field():
    basic_price = ModelField()
    basic_price.name = 'basic_price'
    basic_price.mean = 'Giá'
    basic_price.mode = 'text'
    return basic_price


def get_sale_percent_field():
    sale_percent = ModelField()
    sale_percent.name = 'sale_percent'
    sale_percent.mean = 'Giảm giá'
    sale_percent.mode = 'text'
    return sale_percent


def get_services_field():
    services = ModelField()
    services.name = 'services'
    services.mean = 'Dịch vụ'
    services.mode = 'text'
    return services


def get_feedback_field():
    feedback = ModelField()
    feedback.name = 'feedback'
    feedback.mean = 'feedback'
    feedback.mode = 'text'
    return feedback

def get_level_field():
    level = ModelField()
    level.name = 'level'
    level.mean = 'level'
    level.mode = 'text'
    return level

def get_post_date_field():
    post_date = ModelField()
    post_date.name = 'post_date'
    post_date.mean = 'Ngày đăng'
    post_date.mode = 'date'
    return post_date

def get_image_field():
    image = ModelField()
    image.name = 'image'
    image.mean = 'Hình ảnh'
    image.mode = 'text'
    return image

def get_option_field():
    option = ModelField()
    option.name = 'option'
    option.mean = 'Lựa chọn'
    option.mode = 'text'
    return option

def get_state_fields():
    state = ModelField()
    state.name = 'state'
    state.mean = 'Tình trạng'
    state.mode = 'checkbox'
    return state

def get_description_fields():
    des_description = ModelField()
    des_description.name = 'description'
    des_description.mean = 'Mô tả'
    des_description.mode = 'text'
    return des_description

def get_fields():
    m_id = get_m_id_field()
    name = get_name_field()
    address = get_address_field()
    avatar = get_avatar_field()
    basic_price = get_basic_price_field()
    sale_percent = get_sale_percent_field()
    services = get_services_field()
    feedback = get_feedback_field()
    level = get_level_field()
    post_date = get_post_date_field()
    image = get_image_field()
    option = get_option_field()
    state = get_state_fields()
    des_description = get_description_fields()
    return [m_id, name, address, avatar, basic_price, sale_percent, services, feedback, level,
            post_date,image,option,state, des_description]
