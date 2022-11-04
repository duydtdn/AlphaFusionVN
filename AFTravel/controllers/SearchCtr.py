# def seach..(request)
# get json [key]

# object Destination.objects.filter(post_date__)
# https://stackoverflow.com/questions/4668619/django-database-query-how-to-filter-objects-by-date-range
import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from AFTravel.models import Destination, Place
from AFTravel.controllers.PlaceCtr import get_places

@csrf_exempt
def rq_searchDestination_json(request, place_id, startday, endday):
    if request.method == 'GET':
        place = Place.objects.get(id=place_id)
        place_id = place.id
        place_name = place.name

        if startday == '-':
            # datetime_start = datetime.datetime.now()  # datetime.strptime('1/1/2000', 'dd-mm-YY')
            list_destination = Destination.objects.filter(place_id=place_id)
        else:
            # datetime_start = datetime.datetime.strptime(startday, '%d-%m-%Y')
            # datetime_end = datetime.datetime.strptime(endday, '%d-%m-%Y')
            # list_destination = Destination.objects.filter(id=place_id, post_date__range=[datetime_start, datetime_end])
            list_destination = Destination.objects.filter(place_id=place_id)

    return render(request, '../templates/pages/travel/booking_home.html',
                  {'place_name': place_name,
                   'des_list': list_destination,
                   'places': get_places(),
                   'place_id': place_id
                   })

@csrf_exempt
def rq_search_destination_name_json(request, destination_name, startday, endday):
    if request.method == 'GET':
        # destination = Destination.objects.get(name=destination_name)
        # place_id = place.id
        # place_name = place.name

        if startday == '-':
            # datetime_start = datetime.datetime.now()  # datetime.strptime('1/1/2000', 'dd-mm-YY')
            list_destination = Destination.objects.filter(name=destination_name)
        else:
            datetime_start = datetime.datetime.strptime(startday, '%d-%m-%Y')
            datetime_end = datetime.datetime.strptime(endday, '%d-%m-%Y')
            list_destination = Destination.objects.filter(name=destination_name, post_date__range=[datetime_start, datetime_end])
    return render(request, '../templates/pages/travel/travel_modules/view-des-place-detail.html',
                  {
                   'des_list': list_destination,
                   'places': get_places(),
                   })

@csrf_exempt
def rq_search_destination_name(request):
    if request.method == 'POST':
        request_data = json.loads(request.body.decode('utf-8'))

        if 'tripKeywords' in request_data:
            keyword = str(request_data['tripKeywords'])
            # try:
            # destination = Destination.objects.get(name=name)
            # des_id = destination.id
            # table_title, table_body = RoomCtr.get_table_for_view_destination_place(des_id)
            # des_images = DesImage.objects.filter(destination_id=des_id)
            # des_images_len = len(des_images)
            # des_object = Destination.objects.get(id=des_id)
            # # des_services_reception = DestinationServiceReception.objects.get(destination_id=des_id)
            # des_services_other = DestinationServiceOther.objects.get(destination_id=des_id)
            # except Destination.DoesNotExist:
            #     return 'error'
            place_id_list = []
            place_name = 'Kết quả tìm kiếm'
            result_list = Destination.objects.filter(name__contains=keyword)
            if (len(result_list)) != '1':
                for result in result_list:
                    place_id_list.append(result.place_id)

    return render(request, '../templates/pages/travel/travel_modules/list_des_by_place.html',
                  {
                      'des_list': result_list, 'place_name': place_name
                  }
                  )
    # return render(request, 'bookingWeb/modules/places/view-des-detail.html',
    #               {'des_images': des_images, 'des_images_len': des_images_len,
    #                'table_body': table_body, 'table_title': table_title,
    #                'des_object': des_object,
    #                'des_services_other': des_services_other}
    #               )

@csrf_exempt
def rq_destination_fillter(request):
    if request.method == 'POST':
        request_data = json.loads(request.body.decode('utf-8'))
        place_name = request_data['place_name']
        price_data = request_data['price_list']
        level_data = request_data['level_list']
        price_list = []
        if not price_data:
            price_list.append(0)
            price_list.append(9999999)
        elif price_data is not None:
            for price in price_data:
                if price == "500k" and str(len(price_data)) == "1":
                    price_list.append(0)
                    price_list.append(499)
                    break
                elif price == "500k":
                    price_500 = 500000
                    price_list.append(0)
                    price_list.append(price_500)
                elif price == "500k-1m":
                    price_500 = 500000
                    price_list.append(price_500)
                    price_1m = 1000000
                    price_list.append(price_1m)
                elif price == "1m-2m":
                    price_1m = 1000000
                    price_list.append(price_1m)
                    price_2m = 2000000
                    price_list.append(price_2m)
                elif price == "2m-5m":
                    price_2m = 2000000
                    price_list.append(price_2m)
                    price_5m = 5000000
                    price_list.append(price_5m)
                elif price == "5m":
                    price_5m = 5000000
                    price_list.append(price_5m)
        price_min = min(price_list)
        price_max = max(price_list)
        # place = Place.objects.get(id=place_id)
        # =======
        place = Place.objects.get(name=place_name)
        place_id = place.id
        if not level_data:
            des_list = Destination.objects.filter(place_id=place_id).filter(basic_price__gte=price_min).filter(basic_price__lte=price_max)
        elif level_data is not None and len(level_data) >= 2:
            level_min = min(level_data)
            level_max = max(level_data)
            des_list = Destination.objects.filter(place_id=place_id).filter(basic_price__gte=price_min).filter(
                basic_price__lte=price_max).filter(level__gte=level_min).filter(
                level__lte=level_max)
        else:
            level = level_data[-1]
            des_list = Destination.objects.filter(place_id=place_id).filter(basic_price__gte=price_min).filter(
                basic_price__lte=price_max).filter(level=level)
        return render(request, '../templates/pages/travel/travel_modules/list_des_by_place.html', {
            'place_name': place.name,
            'des_list': des_list,
            'place_id': place_id
        })
    return HttpResponse('error')

@csrf_exempt
def autocomplete(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = Destination.objects.filter(name__startswith=q)
        results = []
        # print(q)
        for r in search_qs:
            results.append(r.name)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

