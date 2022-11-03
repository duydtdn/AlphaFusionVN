from AFTravel.m_models.ModelField import ModelField

def get_m_id_field():
    m_id = ModelField()
    m_id.name = 'm_id'
    m_id.mean = 'm_id'
    m_id.mode = 'text'
    return m_id

def get_place_name_field():
    place_name = ModelField()
    place_name.name = 'place_name'
    place_name.mean = 'Tỉnh/Thành phố'
    place_name.mode = 'text'
    return place_name

def get_avatar_img_field():
    avatar_img = ModelField()
    avatar_img.name = 'place_img'
    avatar_img.mean = 'Hinh anh dia diem'
    avatar_img.mode = 'image'
    return avatar_img

def get_fields():
    m_id = get_m_id_field()
    place_name = get_place_name_field()
    avatar_img = get_avatar_img_field()
    return [m_id, place_name, avatar_img]
