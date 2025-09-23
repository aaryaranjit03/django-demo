import os
import django
import time
from datetime import datetime

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airquality_app.settings')
django.setup()

from monitor.utils import fetch_air_quality
from monitor.models import CityData

def fetch_pune():
    data = fetch_air_quality("Pune", 18.5204, 73.8567)
    CityData.objects.create(**data)
    print(f"{datetime.now()} - Pune data saved: {data}")

if __name__ == "__main__":
    interval_seconds = 600 
    while True:
        fetch_pune()
        time.sleep(interval_seconds)
