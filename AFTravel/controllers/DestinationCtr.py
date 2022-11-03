from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import ModelCtr, RoomCtr
from AFTravel.models import Destination, DesImage, DestinationServiceOther, Room, Place


def get_destination(Destination):
    return ModelCtr.get_all_models(Destination)

def get_all_images_by_id(des_id):
    des_images = []
    for i in ModelCtr.get_all_models(DesImage):
        des_images.append(i.image)
    return des_images

def get_des_by_id(des_id):
    return Destination.objects.filter(id=des_id)

@csrf_exempt
def rq_searchDestination_json(request):
    if request.is_ajax() and request.method == 'POST':
        searchKey = request.GET['destinationSelected']
        listDestination = Destination.objects.filter(name=searchKey)
    return render(request, '../templates/pages/travel/travel_modules/view-des-place-list.html',
                  {'listDestination': listDestination})

# ===============RE QUEST=================
@csrf_exempt
def view_des_place_detail(request, place_id, des_id):
    breadcrumb_pre_path = str(request.path).rsplit('/', 2)[0]
    table_title, table_body = RoomCtr.get_table_for_view_destination_place(des_id)
    des_images = DesImage.objects.filter(destination_id=des_id)
    des_images_len = len(des_images)
    des_object = Destination.objects.get(id=des_id)
    place_object = Place.objects.get(id=place_id)
    # des_services_reception = DestinationServiceReception.objects.get(destination_id=des_id)
    des_services_other = DestinationServiceOther.objects.get(destination_id=des_id)
    return render(request, '../templates/pages/travel/travel_modules/view-des-place-detail.html',
                  {'des_images': des_images, 'des_images_len': des_images_len,
                   'table_body': table_body, 'table_title': table_title,
                   'place_object': place_object,
                   'des_object': des_object,
                   'des_services_other':des_services_other,
                   'breadcrumb_pre_path': breadcrumb_pre_path
                   }
                  )