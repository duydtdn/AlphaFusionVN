from AFTravel.m_models.ModelField import ModelField

def get_m_id_field():
    m_id = ModelField()
    m_id.name = 'm_id'
    m_id.mode = 'm_id'
    m_id.mean = 'text'
    return m_id

def get_voucher_name_field():
    voucher_name = ModelField()
    voucher_name.name = 'voucher_name'
    voucher_name.mean = 'Voucher'
    voucher_name.mode ='text'
    return voucher_name