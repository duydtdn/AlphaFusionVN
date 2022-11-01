from django.shortcuts import render

# Create your views here.
from AFTravel.controllers.PlaceCtr import get_places
from AFWeb.controllers import MenuCtr, BannerCtr


def TravelHome(request):
    list_menu = MenuCtr.get_menu()
    list_carousel = BannerCtr.get_list_banner_by_slide()

    return render(request, '../templates/pages/travel/booking_home.html',
                  {
                      'list_carousel': list_carousel,
                      'list_menu': list_menu,
                      'places': get_places(),

                  }
    )