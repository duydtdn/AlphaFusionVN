from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
# Create your models here.

class Menu(models.Model):
    enabled = models.BooleanField(verbose_name='Kích hoạt', default=True)
    language = models.CharField(max_length=2)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    menu = models.CharField(max_length=120)
    url = models.SlugField(max_length=200)

    def __unicode__(self):
        return '%s' % self.menu
    def __str__(self):
        return self.menu

class TheLoai(models.Model):
    ten = models.CharField(verbose_name='Chuyên mục', max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    # thu_tu = models.IntegerField(default=0)
    # nut_cha = models.IntegerField(default=0, null=True, blank=True)
    def __unicode__(self):
        return '%s' % self.ten
    def __str__(self):
        return self.ten

    def get_absolute_url(self):
        return reverse('AFWeb:news_list', args=[self.slug])

class TinTuc(models.Model):
    the_loai = models.ForeignKey(TheLoai, on_delete=models.CASCADE)
    tieu_de = models.CharField(verbose_name='Tiêu đề',max_length=200, unique=True)
    trich_yeu = models.CharField(verbose_name='Trích yếu', max_length=500, null=True,blank=True)
    noi_dung = RichTextUploadingField(verbose_name='Nội dung',null=True,blank=True)
    ngay_dang = models.DateTimeField(verbose_name='Ngày đăng', db_index=True, auto_now_add=True)

    def news_avartar_image_directory_path(TinTuc, filename):
        dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
        return 'uploads/news/{0}/avartar/{1}'.format(dirname, filename)

    hinh_anh = models.FileField(upload_to=news_avartar_image_directory_path, verbose_name="Hình ảnh",
                              default='', null=True)
    tin_noi_bat = models.BooleanField(verbose_name='Nổi bật',default=False)
    duyet = models.BooleanField(verbose_name='Duyệt', default=True)
    slug = models.SlugField(max_length=500, unique=True)

    def __unicode__(self):
        return '%s' % self.tieu_de

    def __str__(self):
        return self.tieu_de

    def get_absolute_url(self):
        return reverse('AFWeb:news_detail', args=[self.id, self.slug])

# ============== GALLERY ACTIVITIES ==============
class GalleryActivity(models.Model):
    title = models.CharField(default='', max_length=100, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)


class GalleryImages(models.Model):
    url = models.ImageField(upload_to='uploads/imgs/%Y/%m/%d/', default='', null=True)
    gallery_activity = models.ForeignKey(GalleryActivity, on_delete=models.CASCADE)

    # def delete(self, *args, **kwargs):
    #     ModelsCtr.delete_file(str(self.url))
    #     super(GalleryImages, self).delete(*args, **kwargs)

class BannerLoc(models.Model):
    vi_tri = models.CharField(verbose_name='Vị trí', default='default', max_length=150, db_index=True)
    size = models.CharField(default='', max_length=100, blank=True, null=False)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    # thu_tu = models.IntegerField(default=0)
    # nut_cha = models.IntegerField(default=0, null=True, blank=True)
    def __unicode__(self):
        return '%s' % self.vi_tri
    def __str__(self):
        return self.vi_tri

    # def get_absolute_url(self):
    #     return reverse('AFWeb:news_list', args=[self.slug])

class Banner(models.Model):
    banner_loc = models.ForeignKey(BannerLoc, on_delete=models.CASCADE)
    chu_de = models.CharField(verbose_name='Tiêu đề',max_length=200, unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    noi_dung = RichTextUploadingField(verbose_name='Nội dung',null=True,blank=True)
    lien_ket = models.CharField(verbose_name='Liên kết', max_length=200, null=True, blank=True, default='#')
    ngay_dang = models.DateTimeField(verbose_name='Ngày đăng', db_index=True, auto_now_add=True)

    @property
    def get_size(self):
        return self.banner_loc.size
    # kich_thuoc = models.CharField(verbose_name='Size', max_length=50, null=True, blank=True, default=get_size)
    def banner_directory_path(Banner, filename):
        dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
        return 'uploads/banner/{0}/{1}'.format(dirname, filename)

    hinh_anh = models.FileField(upload_to=banner_directory_path, verbose_name="Hình ảnh",
                              default='', null=True)
    slide = models.BooleanField(verbose_name='slide',default=False)
    duyet = models.BooleanField(verbose_name='Duyệt', default=True)

    def __unicode__(self):
        return '%s' % self.chu_de

    def __str__(self):
        return self.chu_de

    def get_absolute_url(self):
        return reverse('AFWeb:news_detail', args=[self.id, self.slug])