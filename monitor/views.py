from django.shortcuts import render
from rest_framework import viewsets
from .models import CityData
from .serializers import CityDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import fetch_air_quality
from django.utils.timezone import localtime
from django.http import JsonResponse


class CityDataViewSet(viewsets.ModelViewSet):
    queryset = CityData.objects.all().order_by('-created_at')
    serializer_class = CityDataSerializer

@api_view(['POST'])
def fetch_and_store_city(request):
    city_name = request.data.get("city_name")
    lat = request.data.get("lat")
    lon = request.data.get("lon")

    if not city_name or lat is None or lon is None:
        return Response({"error": "city_name, lat, and lon are required"}, status=400)

    data = fetch_air_quality(city_name, lat, lon)
    city_entry = CityData.objects.create(**data)
    serializer = CityDataSerializer(city_entry)
    return Response(serializer.data)

def dashboard(request):
    cities = list(CityData.objects.values_list('city_name', flat=True))
    aqi_values = list(CityData.objects.values_list('aqi_value', flat=True))
    context = {
        'cities': cities,
        'aqi_values': aqi_values
    }
    return render(request, 'monitor/dashboard.html', context)

def pune_timeseries(request):
    data = CityData.objects.filter(city_name="Pune").order_by('created_at')
    timestamps = [localtime(d.created_at).strftime("%Y-%m-%d %H:%M") for d in data]
    temps = [d.temperature for d in data]
    humidities = [d.humidity for d in data]
    aqi_values = [d.aqi_value for d in data]

    context = {
        'timestamps': timestamps,
        'temps': temps,
        'humidities': humidities,
        'aqi_values': aqi_values
    }
    return render(request, 'monitor/pune_timeseries.html', context)

def pune_timeseries_data(request):
    data = CityData.objects.filter(city_name="Pune").order_by('created_at')
    timestamps = [localtime(d.created_at).strftime("%Y-%m-%d %H:%M:%S") for d in data]
    temps = [d.temperature for d in data]
    humidities = [d.humidity for d in data]
    aqi_values = [d.aqi_value for d in data]

    return JsonResponse({
        "timestamps": timestamps,
        "temps": temps,
        "humidities": humidities,
        "aqi_values": aqi_values
    })
