from AFTravel.m_models.ModelField import ModelField

def get_id_field():
    id = ModelField()
    id.name = 'id'
    id.mean = 'm_id'
    id.mode = 'text'
    return id

def get_room_category_id_field():
    room_category_id = ModelField()
    room_category_id.name = 'name'
    room_category_id.mean = 'Loại Phòng'
    room_category_id.mode = 'combobox'
    return room_category_id

def get_room_name_fields():
    room_name = ModelField()
    room_name.name = 'name'
    room_name.mean = 'Chi tiết phòng'
    room_name.mode = 'text'
    return room_name

def get_room_avartar_img_fields():
    room_avartar_img = ModelField()
    room_avartar_img.name = 'avartar'
    room_avartar_img.mean = 'Hình ảnh'
    room_avartar_img.mode = 'text'
    return room_avartar_img

def get_room_option_fields():
    room_option = ModelField()
    room_option.name = 'option'
    room_option.mean = 'Lựa chọn'
    room_option.mode = 'text'
    return room_option

def get_room_price_fields():
    room_price = ModelField()
    room_price.name = 'room_price'
    room_price.mean = 'Giá phòng'
    room_price.mode = 'text'
    return room_price

def get_room_area_fields():
    room_area = ModelField()
    room_area.name = 'room_area'
    room_area.mean = 'Diện tích'
    room_area.mode = 'text'
    return room_area

def get_room_amount_of_people_fields():
    room_amount_of_people = ModelField()
    room_amount_of_people.name = 'room_amount_of_people'
    room_amount_of_people.mean = 'Số Người'
    room_amount_of_people.mode = 'text'
    return room_amount_of_people
# def get_room_air_conditioning_fields():
#     room_air_conditioning = ModelField()
#     room_air_conditioning.name = 'room_air_conditioning'
#     room_air_conditioning.mean = 'Điều hòa'
#     room_air_conditioning.mode = 'checkbox'
#     return room_air_conditioning
#
# def get_room_bathtub_fields():
#     room_bathtub = ModelField()
#     room_bathtub.name = 'room_bathtub'
#     room_bathtub.mean = 'Bồn tắm'
#     room_bathtub.mode = 'checkbox'
#     return room_bathtub
#
# def get_room_minibar_fields():
#     room_minibar = ModelField()
#     room_minibar.name = 'room_minibar'
#     room_minibar.mean = 'Mini Bar'
#     room_minibar.mode = 'checkbox'
#     return room_minibar

def get_fields_for_view_destination_place():
    id = get_id_field()
    room_category_id = get_room_category_id_field()
    room_name = get_room_name_fields()
    room_option = get_room_option_fields()
    room_amount_of_people = get_room_amount_of_people_fields()
    room_price = get_room_price_fields()
    room_area = get_room_area_fields()
    room_avatar = get_room_avartar_img_fields()
    return [id, room_name, room_option, room_amount_of_people, room_price, room_area, room_avatar]

def get_fields():
    id = get_id_field()
    room_category_id = get_room_category_id_field()
    room_name = get_room_name_fields()
    room_avartar_img = get_room_avartar_img_fields()
    room_option = get_room_option_fields()
    room_price = get_room_price_fields()
    # room_air_conditioning = get_room_air_conditioning_fields()
    # room_bathtub = get_room_bathtub_fields()
    # room_minibar = get_room_minibar_fields()
    return [id, room_category_id, room_name, room_avartar_img, room_option, room_price]
            # , room_air_conditioning, room_bathtub, room_minibar]
