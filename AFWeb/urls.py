from django.conf.urls import url
from django.urls import include
from django.urls import path
from AFWeb import views

app_name = "AFWeb"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^en/$', views.index, name='news_list'),
    path('news/detail/<str:slug>......<int:id>/', views.news_detail_view, name='news_detail'),
    path('news/search/', views.SearchResultsView.as_view(), name='rq-search-by-keyword'),
]