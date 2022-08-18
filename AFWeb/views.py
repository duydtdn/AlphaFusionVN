from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from AFWeb.controllers import BannerCtr
from django.views.generic import ListView
from AFWeb.models import TheLoai, TinTuc, Menu
def index(request):
    # create_user_session(request)
    list_carousel = BannerCtr.get_list_banner_by_slide()
    return render(request, '../templates/index.html',
                  {
                      # 'home_about': about.get_about_show_index_page()[:1],
                      'list_carousel': list_carousel,
                   }
                  )

class SearchResultsView(ListView):
    model = TinTuc
    template_name = '../templates/pages/news.html'
    context_object_name = 'news_by_category'
    paginate_by = 2
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        news_by_category = TinTuc.objects.filter(
            Q(tieu_de__icontains=query) | Q(trich_yeu__icontains=query)
        )
        context_object_name = news_by_category
        return context_object_name