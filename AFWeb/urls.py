from django.conf.urls import url
from django.urls import include
from django.urls import path
from AFWeb import views

app_name = "AFWeb"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^en/$', views.index, name='news_list'),
    path('news/search/', views.SearchResultsView.as_view(), name='rq-search-by-keyword'),
]