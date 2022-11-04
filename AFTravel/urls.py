from django.conf.urls import url
from django.urls import include
from django.urls import path
from AFTravel import views
from .controllers import SearchCtr

app_name = "AFTravel"
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.TravelHome, name='index'),
    # path('search', views.SearchResultsView.as_view(), name='rq-search-by-keyword'),
    url(r'^search/rq-search-json/(?P<place_id>[0-9]+)/(?P<startday>[0-9-]+)/(?P<endday>[0-9-]+)/$', SearchCtr.rq_searchDestination_json, name='rq-search-json'),
]