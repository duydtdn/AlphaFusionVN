from django.conf.urls import url
from django.urls import include
from django.urls import path
from AFTravel import views

app_name = "AFTravel"
urlpatterns = [
    url(r'^$', views.index, name='index'),
]