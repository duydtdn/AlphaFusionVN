from AFWeb.models import BannerLoc, Banner

def get_banner_location_id_by_vitri(vi_tri):
    m_id = BannerLoc.objects.filter(vi_tri=vi_tri).first().id
    return int(m_id)

def get_list_banner_by_banner_loc_id(banner_loc_id):
    return Banner.objects.filter(banner_loc=banner_loc_id).order_by('-id')

def get_list_banner_by_banner_loc(banner_loc):
    banner_loc_id = get_banner_location_id_by_vitri(banner_loc)
    banner_list = get_list_banner_by_banner_loc_id(banner_loc_id)
    return banner_list

def get_banner_img(banner_id):
    return Banner.objects.get(id=banner_id)

def get_list_banner_by_slide():
    banner_list = Banner.objects.filter(slide=True).order_by('-id')
    return banner_list