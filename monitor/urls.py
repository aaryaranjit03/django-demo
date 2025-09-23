from django.urls import path, include
from rest_framework import routers
from .views import CityDataViewSet
from .views import fetch_and_store_city
from .views import dashboard
from .views import pune_timeseries_data
from .views import pune_timeseries

router = routers.DefaultRouter()
router.register(r'citydata', CityDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('fetch_city/', fetch_and_store_city, name='fetch_city'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/pune/', pune_timeseries, name='pune_timeseries'),
    path('dashboard/pune/data/', pune_timeseries_data, name='pune_timeseries_data'),
    
]

