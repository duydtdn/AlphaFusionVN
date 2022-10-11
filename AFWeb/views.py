from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.db.models import Q
from AFWeb.controllers import BannerCtr, NewsCtr, ClientsCtr, MenuCtr
from django.views.generic import ListView
from AFWeb.models import TheLoai, TinTuc, Menu
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    # create_user_session(request)
    list_menu = MenuCtr.get_menu()
    list_carousel = BannerCtr.get_list_banner_by_slide()
    list_news, category_name, category_slug = NewsCtr.get_list_news_by_category('Tin tức - Sự kiện')
    list_clients = ClientsCtr.get_clients()
    return render(request, '../templates/index.html',
                  {
                      # 'home_about': about.get_about_show_index_page()[:1],
                      'list_carousel': list_carousel,
                      'list_menu': list_menu,
                      'list_news': list_news,
                      'category_name': category_name,
                      'category_slug': category_slug,
                      'list_clients': list_clients
                   }
                  )
def get_news_by_category(request, category_slug):
    categories_id = TheLoai.objects.filter(slug=category_slug).first().id
    list_news_by_category = TinTuc.objects.filter(the_loai_id=categories_id).order_by('id')
    list_menu = Menu.objects.filter(enabled=True, parent__isnull=True)
    if category_slug == 'About':
        # home_about = home_view.get_about_show_index_page('About')
        context = {
            'list_menu': list_menu,
            # 'home_about': home_about,
        }
        return render(request, '../templates/pages/about_page.html', context)
    page = request.GET.get('page', 1)
    paginator = Paginator(list_news_by_category, 10)
    try:
        news_by_category = paginator.page(page)
    except PageNotAnInteger:
        news_by_category = paginator.page(1)
    except EmptyPage:
        news_by_category = paginator.page(paginator.num_pages)
    # if category_slug:
    #     category = get_object_or_404(TheLoai, slug=category_slug)
        # blogs_by_categories = Blog.objects.filter(category=category)

    context = {
        'news_by_category': news_by_category,
        'list_menu': list_menu
    }
    return render(request, '../templates/pages/news.html', context)

def news_detail_view(request, slug, id):
    # list_news = news.get_news()
    news = TinTuc.objects.filter(id=id, slug=slug)
    context = {
        'news': news,
        # 'recent_blogs': recent_news,
    }
    return render(request, '../templates/pages/news.html', context)

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