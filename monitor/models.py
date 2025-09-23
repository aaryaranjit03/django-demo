from django.db import models

class CityData(models.Model):
    city_name = models.CharField(max_length=100)
    aqi_value = models.IntegerField()       # numeric AQI 1–5
    aqi_text = models.CharField(max_length=20, default="Unknown")  # Good, Fair, etc.
    temperature = models.FloatField()
    humidity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city_name} - AQI {self.aqi_text} ({self.aqi_value})"
        # return f"{self.city_name} - AQI {self.aqi}, Temp: {self.temperature}°C, Humidity: {self.humidity}%"

