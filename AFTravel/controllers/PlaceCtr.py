from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from AFTravel.models import Place, Destination
from AFTravel.controllers import ModelCtr


def get_places():
    return ModelCtr.get_all_models(Place)

def get_all_name_place(des_id):
    list_name_place = []
    for p in get_places():
        list_name_place.append(p.name)

    return list_name_place[des_id]

def get_place_by_id(place_id):
    return Place.objects.filter(id=place_id)

#===============REQUEST=================
@csrf_exempt
def view_des_place_list(request, place_id):
    des_list = Destination.objects.filter(place_id=place_id)
    place = Place.objects.get(id=place_id)
    place_name = place.name
    place_title = "Điểm đến tại " + place.name

    return render(request, '../templates/pages/travel/travel_modules/view-des-place-list.html',
                  {
                      'des_list': des_list, 'place_name':place_name, 'place_title': place_title, 'places': get_places()

                   }
                  )

@csrf_exempt
def filter_des_place_detail(request):
    des_filter_list = get_places()
    return render(request, 'bookingWeb/home/index.html', {'des_filter_list': des_filter_list})