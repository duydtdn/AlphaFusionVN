import datetime
from datetime import date
from macpath import join

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt

from AFTravel.models import Room, Destination
import json
import time
def name_of_weeks_convert(str):
    if str == 'Monday':
        return "Thứ Hai"
    elif str == 'Tueday':
        return "Thứ Ba"
    elif str == 'Wednesday':
        return "Thứ Tư"
    elif str == 'Thursday':
        return "Thứ Năm"
    elif str == 'Friday':
        return "Thứ Sáu"
    elif str == 'Saturday':
        return "Thứ Bảy"
    else:
        return "Chủ Nhật"

def dateconvert(str):
    parse_name_of_weeks = parse_date(str).strftime("%A")
    name_of_weeks = name_of_weeks_convert(parse_name_of_weeks)
    day = parse_date(str).strftime("Ngày %d, tháng %m, năm %Y")
    return name_of_weeks, day

@csrf_exempt
def step1(request, des_room_id, des_id, dateCheckIn, dateCheckOut):
    if request.method == 'GET':
        room_obj = Room.objects.get(id=des_room_id,destination_id=des_id)
        des_obj = Destination.objects.get(id=des_id)
        return render(request, '../templates/pages/travel/travel_modules/view-reservation-form.html',
                          {
                              'room_obj': room_obj,
                              'des_obj': des_obj,
                          }
                      )
    return HttpResponse('error')
@csrf_exempt
def view_reservation_form(request, des_id, room_id, dateCheckIn,dateCheckOut):
    des_room_id = room_id
    des_id = des_id
    room_obj = Room.objects.get(id=des_room_id, destination_id=des_id)
    des_obj = Destination.objects.get(id=des_id)
    data_date_checkin = dateCheckIn
    data_date_checkout = dateCheckOut
    start_date = datetime.datetime.strptime(data_date_checkin, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(data_date_checkout, "%Y-%m-%d")
    sum_night = abs((end_date - start_date).days)
    try:
        name_of_weeks_checkin, dateCheckIn = dateconvert(data_date_checkin)
        name_of_weeks_checkout, dateCheckOut = dateconvert(data_date_checkout)
    except:
        raise Exception('Convert day error')
    return render(request, '../templates/pages/travel/travel_modules/view-reservation-form.html',
                  {
                      'room_obj': room_obj,
                      'des_obj': des_obj,
                      'name_of_weeks_checkin': name_of_weeks_checkin,
                      'name_of_weeks_checkout': name_of_weeks_checkout,
                      'dateCheckIn': dateCheckIn,
                      'dateCheckOut': dateCheckOut,
                      'sum_night': sum_night,
                  }
                  )

@csrf_exempt
def rq_reservation(request):
    if request.method == 'POST':
        dataJson = json.loads(request.body.decode('utf-8'))
        des_room_id = dataJson['m_id']
        des_id = dataJson['des_id']
        room_obj = Room.objects.get(id=des_room_id, destination_id=des_id)
        des_obj = Destination.objects.get(id=des_id)
        data_date_checkin = dataJson['dateCheckIn']
        data_date_checkout = dataJson['dateCheckOut']
        start_date = datetime.datetime.strptime(data_date_checkin,"%Y-%m-%d")
        end_date = datetime.datetime.strptime(data_date_checkout, "%Y-%m-%d")
        sum_night = abs((end_date - start_date).days)
        try:
            name_of_weeks_checkin, dateCheckIn = dateconvert(data_date_checkin)
            name_of_weeks_checkout, dateCheckOut = dateconvert(data_date_checkout)
        except:
            raise Exception('Convert day error')

        # datecheckin_formated = ''.join(dateCheckIn.split('-')[::1]) # [::-1] La reverse
        # datecheckout_formated = ''.join(dateCheckOut.split('-')[::1])
        return render(request, '../templates/pages/travel/travel_modules/view-reservation-form.html',
                      {
                          'room_obj': room_obj,
                          'des_obj': des_obj,
                          'name_of_weeks_checkin': name_of_weeks_checkin,
                          'name_of_weeks_checkout': name_of_weeks_checkout,
                          'dateCheckIn': dateCheckIn,
                          'dateCheckOut': dateCheckOut,
                          'sum_night': sum_night,
                      }
                      )
    return HttpResponse('error')

@csrf_exempt
def rq_update_reservation(request):
    if request.method == 'POST':
        dataJson = json.loads(request.body.decode('utf-8'))
        # des_room_id = dataJson['m_id']
        # des_id = dataJson['des_id']
        # room_obj = Room.objects.get(id=des_room_id, destination_id=des_id)
        # des_obj = Destination.objects.get(id=des_id)
        data_date_checkin = dataJson['dateCheckIn']
        data_date_checkout = dataJson['dateCheckOut']
        start_date = datetime.datetime.strptime(data_date_checkin,"%Y-%m-%d")
        end_date = datetime.datetime.strptime(data_date_checkout, "%Y-%m-%d")
        sum_night = abs((end_date - start_date).days)
        try:
            name_of_weeks_checkin, dateCheckIn = dateconvert(data_date_checkin)
            name_of_weeks_checkout, dateCheckOut = dateconvert(data_date_checkout)
        except:
            raise Exception('Convert day error')

        # datecheckin_formated = ''.join(dateCheckIn.split('-')[::1]) # [::-1] La reverse
        # datecheckout_formated = ''.join(dateCheckOut.split('-')[::1])
        return render(request, '../templates/pages/travel/travel_modules/des_info_reservation.html',
                      {
                          # 'room_obj': room_obj,
                          # 'des_obj': des_obj,
                          # 'name_of_weeks_checkin': name_of_weeks_checkin,
                          # 'name_of_weeks_checkout': name_of_weeks_checkout,
                          # 'dateCheckIn': dateCheckIn,
                          # 'dateCheckOut': dateCheckOut,
                          'sum_night': sum_night,
                      }
                      )
    return HttpResponse('error')