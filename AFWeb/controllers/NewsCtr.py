from AFWeb.controllers import CategoryCtr
from AFWeb.models import TinTuc

def get_list_news_by_category_id(category_id):
    return TinTuc.objects.filter(the_loai=category_id).order_by('-ngay_dang', '-id')

def get_list_news_by_category(category_name):
    category_id, category_slug = CategoryCtr.get_category_id_by_name(category_name)
    news_list = get_list_news_by_category_id(category_id)
    return news_list, category_name, category_slug