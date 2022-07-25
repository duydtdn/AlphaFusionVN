from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from AFWeb.controllers import BannerCtr


def index(request):
    # create_user_session(request)
    list_carousel = BannerCtr.get_list_banner_by_slide()
    return render(request, '../templates/index.html',
                  {
                      # 'home_about': about.get_about_show_index_page()[:1],
                      'list_carousel': list_carousel,
                   }
                  )