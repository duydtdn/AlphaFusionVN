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
    path('search/rq-search-json/<int:place_id>/<str:startday>/<str:endday>/', SearchCtr.rq_searchDestination_json, name='rq-search-json'),

]