from django.urls import path

from weather_control.views import (create_new_weather_type, update_weather_type, delete_weather_type,
                                   deactivate_weather_type, activate_weather_type, get_all_weather_types,
                                   get_all_active_weather_types, get_weather_type_by_id)

urlpatterns = [
    path("create", create_new_weather_type),
    path("update/<str:pk>", update_weather_type),
    path("delete/<str:pk>", delete_weather_type),
    path("deactivate/<str:pk>", deactivate_weather_type),
    path("activate/<str:pk>", activate_weather_type),
    path("list", get_all_weather_types),
    path("list/active", get_all_active_weather_types),
    path("<str:pk>", get_weather_type_by_id),
]
