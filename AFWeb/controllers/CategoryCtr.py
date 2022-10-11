from AFWeb.models import TheLoai

def get_objects_by_parrent(parrent):
    list_obj = TheLoai.objects.filter(nut_cha=parrent)
    return list_obj

def get_titles_category(parent_title):
    parent = TheLoai.objects.filter(ten__contains=parent_title).first()
    objs = get_objects_by_parrent(parent.id).order_by('thu_tu')
    categorys_title = []
    for obj in objs:
        categorys_title.append(obj.ten)
    return categorys_title

def get_category_id_by_name(name):
    m_id = TheLoai.objects.filter(ten=name).first().id
    cat_slug = TheLoai.objects.filter(ten=name).first().slug
    return int(m_id), cat_slug

def get_category_by_id(id):
    m_id = TheLoai.objects.filter(id=id)
    return m_id