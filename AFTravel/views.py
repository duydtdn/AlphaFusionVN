from django.shortcuts import render
from django.db.models import Max
# Create your views here.
from AFTravel.controllers import PlaceCtr, DestinationCtr
from AFTravel.models import Destination
from AFWeb.controllers import MenuCtr, BannerCtr


def TravelHome(request):
    list_menu = MenuCtr.get_menu()
    list_carousel = BannerCtr.get_list_banner_by_slide()
    first, second = DestinationCtr.get_newest_des()
    return render(request, '../templates/pages/travel/booking_home.html',
                  {
                      'list_carousel': list_carousel,
                      'list_menu': list_menu,
                      'places': PlaceCtr.get_places(),
                      'des_first': first,
                      'des_second': second
                  }
    )