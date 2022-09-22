from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from base import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", include("user_control.urls")),
    path("api/weather/", include("weather_control.urls")),
    path("api/product/", include("product_control.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
