import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from AFTravel.models import Room, BedCategory, RoomImage
import ModelCtr
from AFTravel.m_models import RoomAst
import html.parser

def get_all_room():
    return ModelCtr.get_all_models(Room)

def get_room_by_id(des_id):
    return Room.objects.filter(destination_id=des_id)

@csrf_exempt
def get_table_for_view_destination_place(des_id):
    table_fields = RoomAst.get_fields_for_view_destination_place()
    # Get Tilte
    table_title = []
    for field in table_fields:
        table_title.append(field.mean)
    # Get Content
    table_body = []
    # all_objs = ModelCtr.get_all_models(Room)
    all_objs = get_room_by_id(des_id=des_id)
    for obj in all_objs:
        obj_values = []
        for field in table_fields:
            value = str(obj.__getattribute__(field.name))
            if field.name == 'option':
                value = value.replace(';', '<br />')
            obj_values.append(value)
        table_body.append(obj_values)

    return table_title, table_body


# def get_table():
#     table_fields = RoomAst.get_fields()
#     #Get Tilte
#     table_title = []
#     for field in table_fields:
#         table_title.append(field.mean)
#     #Get Content
#     table_body = []
#     all_objs = ModelCtr.get_all_models(Room)
#     for obj in all_objs:
#         obj_values = []
#         for field in table_fields:
#             obj_values.append(str(obj.__getattribute__(field.name)))
#         table_body.append(obj_values)
#
#     return table_title, table_body

# ===============REQUEST=================
@csrf_exempt
def view_room_list(request):
    table_title, table_body = get_table_for_view_destination_place()
    return render(request, 'bookingWeb/modules/room/components/room-table.html',
                  {
                      'table_title': table_title,
                      'table_body': table_body,
                  })


@csrf_exempt
def rq_room_detail(request):
    dataJson = json.loads(request.body.decode('utf-8'))
    m_id = dataJson['m_id']
    # Get data from model (room_detail)
    # Temp use Room model
    room_detail = Room.objects.get(pk=m_id)
    room_image = RoomImage.objects.filter(room_id=m_id)
    bed_object = BedCategory.objects.get(id=m_id)
    return render(request, '../templates/pages/travel/travel_modules/rp_room_detail.html',
                  {
                      'room_detail': room_detail,
                      'bed_object':bed_object,
                      'room_image':room_image,
                  })
