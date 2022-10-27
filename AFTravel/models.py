from datetime import datetime
from PIL import Image
from bs4 import BeautifulSoup
from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(default='', max_length=256, null=True, blank=True)
    def place_avartar_image_directory_path(Place, filename):
        return 'uploads/places/{0}/{1}'.format(Place.id, filename)
    avatar_img = models.ImageField(upload_to=place_avartar_image_directory_path, default='', null=True)
    class Meta:
        verbose_name_plural = 'Tỉnh/thành phố'
    def __str__(self):
        return 'Tỉnh/Thành: {}'.format(self.name)

class Destination(models.Model):
    place = models.ForeignKey(Place,verbose_name="Chọn Tỉnh/thành", on_delete=models.CASCADE)
    name = models.CharField(default='',verbose_name="Điểm đến", max_length=256, null=True, blank=True)
    address = models.CharField(default='',verbose_name="Địa chỉ", max_length=256, null=True, blank=True)
    # geolocation = map_fields.GeoLocationField(max_length=100)
    def destination_avartar_image_directory_path(Destination, filename):
        dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
        return 'uploads/destination/{0}/avartar/{1}'.format(dirname, filename)
    avatar = models.FileField(upload_to=destination_avartar_image_directory_path,verbose_name="Hình ảnh đại diện", default='', null=True)
    def save(self, force_insert=False, force_update=False):
        super(Destination, self).save(force_insert, force_update)
        if self.id is not None:
            # previous = Destination.objects.get(id=self.id)
            # if self.avatar and self.avatar != previous.avatar:
            if self.avatar:
                image = Image.open(self.avatar.path)
                image = image.resize((165, 165), Image.ANTIALIAS)
                image.save(self.avatar.path)
    basic_price = models.IntegerField(default=0,null=True, blank=True)
    sale_percent = models.FloatField(default=0,null=True, blank=True)
    # SERVICES_CHOICES = (
    #     ('WIFI', 'WIFI'),
    #     ('RES', 'NHÀ HÀNG'),
    #     ('LAU', 'GIẶT ỦI'),
    # )
    #
    # services = MultiSelectField(choices=SERVICES_CHOICES, )
    # def is_upperclass(self):
    #     return self.services in (self.JUNIOR, self.SENIOR)
    feedback = models.CharField(default='', max_length=256, null=True, blank=True)
    level = models.IntegerField(default=1,null=True, blank=True)
    post_date = models.DateField(auto_now_add=True, blank=True, null=True)
    state = models.BooleanField(default=True, blank=True)
    des_description = RichTextField()
    def __str__(self):
        return 'Destination: {}'.format(self.name)

class DesImage(models.Model):
    destination = models.ForeignKey(Destination,verbose_name="Điểm đến", on_delete=models.CASCADE)
    def destination_image_directory_path(destination, filename):
        return 'uploads/destination/{0}/{1}'.format(destination.destination_id, filename)
    image = models.ImageField(upload_to=destination_image_directory_path, verbose_name="Tải hình ảnh", default='', null=True)
    class Meta:
        verbose_name_plural = 'Hình ảnh'

# class Notification(models.Model):
#     users = models.ManyToManyField(User, through='UserNotification')
#     title = models.CharField(default='Can Travel',verbose_name="Tiêu đề", max_length=256, null=True, blank=True)
#     message = RichTextField()
#     def save(self, *args, **kwargs):
#         soup = BeautifulSoup(self.message)
#         message_notification = soup.get_text()
#         headings = self.title
#         data = {
#             "app_id": "0e403062-5d08-4805-a39c-29845b177287",
#             "included_segments": ["All"],
#             "contents": {"en": message_notification},
#             "headings": {"en": headings},
#         }
#         requests.post(
#             "https://onesignal.com/api/v1/notifications",
#             headers={"Authorization": "Basic ODI5YmM5YzYtZTk1ZS00MzlmLTg1ODQtY2Q3MDVhOGEwYjgy"},
#             json=data
#         )
#         return super(Notification, self).save(*args, **kwargs)
#     class Meta:
#         verbose_name_plural = 'Thông báo'
#     def __str__(self):
#         return 'Notification: {}'.format(self.title)

# class UserNotification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True, blank=True, null=True)
#     state = models.BooleanField(default=False,verbose_name="unread", blank=True)

class Voucher(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    # name = models.CharField(default='', max_length=100, null=True, blank=True)
    price = models.IntegerField(default=0,null=True, blank=True)
    sale_price = models.IntegerField(default=0,null=True, blank=True)
    date_apply = models.DateField(auto_now_add=True, blank=True, null=True)
    date_expiry = models.DateField(auto_now_add=True, blank=True, null=True)
    def voucher_avartar_image_directory_path(Voucher, filename):
        return 'uploads/places/destination/voucher/{0}/{1}'.format(Voucher.id, filename)
    voucher_image = models.FileField(upload_to=voucher_avartar_image_directory_path, default='', null=True)
    def save(self, force_insert=False, force_update=False):
        super(Voucher, self).save(force_insert, force_update)
        if self.id is not None:
            previous = Destination.objects.get(id=self.id)
            if self.voucher_image and self.voucher_image != previous.avatar:
                image = Image.open(self.voucher_image.path)
                image = image.resize((347, 348), Image.ANTIALIAS)
                image.save(self.voucher_image.path)
    hot_deal = models.BooleanField(default=False, blank=True)
    def __str__(self):
        return 'Voucher: {}'.format(self.destination.name)

class DestinationOption(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    cancellation = models.BooleanField(default=False,verbose_name="Hủy phòng", blank=True)
    returnmoney = models.BooleanField(default=False,verbose_name="Hoàn trả tiền", blank=True)
    brunch = models.BooleanField(default=True,verbose_name="Bữa ăn kèm theo", blank=True)
    class Meta:
        verbose_name_plural = 'TÙY CHỌN'

class DestinationServiceOther(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    non_smoking = models.BooleanField(default=True,verbose_name="Không thuốc lá", blank=True)
    elevator = models.BooleanField(default=True,verbose_name="Thang máy", blank=True)
    soundproofing = models.BooleanField(default=True,verbose_name="Phòng cách âm", blank=True)
    currency_exchange = models.BooleanField(default=True,verbose_name="Dịch vụ đổi tiền", blank=True)
    heater = models.BooleanField(default=False,verbose_name="Phòng có lò sưởi", blank=True)
    parking = models.BooleanField(default=True, verbose_name="Phòng có lò sưởi", blank=True)
    wifi = models.BooleanField(default=True,verbose_name="WIFI", blank=True)
    restaurant = models.BooleanField(default=True,verbose_name="Nhà hàng", blank=True)
    laudry = models.BooleanField(default=True,verbose_name="Dịch vụ giặt ủi", blank=True)
    class Meta:
        verbose_name_plural = 'Dịch vụ'

class BedCategory(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=100, null=True, blank=True)
    size = models.CharField(default='', max_length=50, null=True, blank=True)
    def __str__(self):
        return 'Loại giường: {}'.format(self.name)

class Room(models.Model):
    name = models.CharField(default='', max_length=100, null=True, blank=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    # room_category = models.ForeignKey(RoomCategory, on_delete=models.DO_NOTHING)
    bed_category = models.ForeignKey(BedCategory, on_delete=models.DO_NOTHING)
    option = models.CharField(default='', max_length=100, null=True, blank=True)
    room_price = models.IntegerField(default=0,null=True, blank=True)
    room_area = models.CharField(default='', max_length=20, null=True, blank=True)
    room_amount_of_people = models.CharField(default='2', max_length=50, null=True, blank=True)
    room_description = models.CharField(default='', max_length=500, null=True, blank=True)
    device = models.CharField(default='', max_length=500, null=True, blank=True)
    note = models.CharField(default='', max_length=500, null=True, blank=True)
    def room_image_directory_path(destination, filename):
        return 'uploads/destination/{0}/room/{1}'.format(destination.destination_id, filename)
    avartar = models.ImageField(upload_to= room_image_directory_path, default='', null=True)
    # air_conditioning = models.BooleanField(default=True, blank=True)
    # bathtub = models.BooleanField(default=True, blank=True)
    # mini_bar = models.BooleanField(default=True, blank=True)
    def __str__(self):
        return 'Hạng Phòng: {}'.format(self.name)

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    def room_image_directory_path(room, filename):
        return 'uploads/room/{0}/{1}'.format(room.room_id, filename)
    room_image = models.ImageField(upload_to=room_image_directory_path, default='', null=True)

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    date_checkin = models.DateField(auto_now_add=True, blank=True, null=False)
    date_checkout = models.DateField(auto_now_add=True, blank=True, null=False)
    room_amount = models.IntegerField(default=1,null=True, blank=True)
    room_category = models.CharField(default='1', max_length=10, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Đặt phòng'