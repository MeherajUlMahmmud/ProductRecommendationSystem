from django.db import models


class WeatherModel(models.Model):
    weather_type = models.CharField(max_length=100)
    min_temp = models.FloatField()
    max_temp = models.FloatField()
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.weather_type

    class Meta:
        verbose_name = "Weather Type"
        verbose_name_plural = "Weather Types"
