from rest_framework import serializers

from weather_control.models import WeatherModel


class WeatherSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    weather_type = serializers.CharField()
    min_temp = serializers.FloatField()
    max_temp = serializers.FloatField()
    is_active = serializers.BooleanField()
    is_deleted = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = WeatherModel
        fields = '__all__'
