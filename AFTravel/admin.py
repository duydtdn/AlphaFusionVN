from django.contrib import admin
from AFTravel import models
from .models import DesImage, RoomImage, DestinationServiceOther, Destination
# from onesignal import OneSignal, FilterNotification, Filter, SegmentNotification
# Register your models here.

class ServicesInline(admin.TabularInline):
    model = DestinationServiceOther
    extra = 1

class ImageInline(admin.StackedInline):
    model = DesImage
    extra = 1

class DestinationAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ServicesInline]

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            DesImage.image.create(image=afile)

class RoomInline(admin.StackedInline):
    model = RoomImage
    extra = 1

class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomInline]

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('image'):
            obj.image.create(image=afile)

admin.site.register(models.Place)
admin.site.register(models.Destination,DestinationAdmin)
admin.site.register(models.DestinationServiceOther)
# admin.site.register(models.DestinationServiceReception)
admin.site.register(models.Room,RoomAdmin)
admin.site.register(models.DesImage)
admin.site.register(models.Voucher)
admin.site.register(models.BedCategory)