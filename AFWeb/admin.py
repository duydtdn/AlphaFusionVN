from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from django_mptt_admin.admin import DjangoMpttAdmin
from AFWeb.models import *
from AFWeb.forms import TinTucForm
# Register your models here.

admin.site.site_header = 'AlphaFusionVN'
# class TheLoaiInline(admin.TabularInline):
#     model = TheLoai

# class TheLoaiMPTTModelAdmin(DjangoMpttAdmin):
#     def is_drag_and_drop_enabled(self):
#         return True

class TinTucAdmin(admin.ModelAdmin):
    # search_fields = ('tieu_de', )
    # exclude = ['ngay_dang']
    # prepopulated_fields = {'slug': ('tieu_de',)}
    # list_display = ('ngay_dang', 'tieu_de', 'duyet')
    # list_editable = ('ngay_dang', 'tieu_de', 'duyet')
    prepopulated_fields = {'slug': ('tieu_de',)}
    form = TinTucForm

# class BannerLocAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('vi_tri',)}

class BannerAdmin(admin.ModelAdmin):
    search_fields = ('chu_de', )
    exclude = ['ngay_dang']
    prepopulated_fields = {'slug': ('chu_de',)}
    list_display = ('chu_de', 'get_size')

class TheLoaiAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('ten',)}

admin.site.register(TinTuc, TinTucAdmin)
admin.site.register(TheLoai, TheLoaiAdmin)
admin.site.register(BannerLoc)
admin.site.register(Banner, BannerAdmin)
# admin.site.register(Client, ClientAdmin)
admin.site.register(GalleryActivity)
admin.site.register(Menu)
admin.site.register(Client)