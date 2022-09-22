from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from weather_control.models import WeatherModel
from weather_control.serializer import WeatherSerializer


@api_view(["POST"])
def create_new_weather_type(request):
    print(request.data)
    data = request.data
    weather_type = data.get("weather_type")
    min_temp = data.get("min_temp")
    max_temp = data.get("max_temp")

    if not weather_type:
        return Response({"error": "Weather Type is required"}, status=HTTP_400_BAD_REQUEST)

    if not min_temp:
        return Response({"error": "Min temp is required"}, status=HTTP_400_BAD_REQUEST)

    if not max_temp:
        return Response({"error": "Max temp is required"}, status=HTTP_400_BAD_REQUEST)

    if max_temp < min_temp:
        return Response({"error": "Max temp must be greater than min temp"}, status=HTTP_400_BAD_REQUEST)

    weather = WeatherModel.objects.create(
        weather_type=weather_type, min_temp=min_temp, max_temp=max_temp
    )
    weather.save()

    return Response(
        {"message": "Weather type created successfully"},
        status=HTTP_201_CREATED,
    )


@api_view(["PATCH"])
def update_weather_type(request, pk):
    print(request.data)
    data = request.data
    weather_type = data.get("weather_type")
    min_temp = data.get("min_temp")
    max_temp = data.get("max_temp")

    if not weather_type:
        return Response({"error": "Weather Type is required"}, status=HTTP_400_BAD_REQUEST)

    if not min_temp:
        return Response({"error": "Min temp is required"}, status=HTTP_400_BAD_REQUEST)

    if not max_temp:
        return Response({"error": "Max temp is required"}, status=HTTP_400_BAD_REQUEST)

    if max_temp < min_temp:
        return Response({"error": "Max temp must be greater than min temp"}, status=HTTP_400_BAD_REQUEST)

    if not WeatherModel.objects.filter(id=pk).exists():
        return Response(
            {"error": "Weather type does not exists"}, status=HTTP_400_BAD_REQUEST
        )

    WeatherModel.objects.filter(id=pk).update(
        weather_type=weather_type, min_temp=min_temp, max_temp=max_temp
    )

    return Response(
        {"message": "Weather type updated successfully"},
        status=HTTP_200_OK,
    )


@api_view(["DELETE"])
def delete_weather_type(request, pk):
    if not WeatherModel.objects.filter(id=pk).exists():
        return Response(
            {"error": "Weather type does not exists"}, status=HTTP_400_BAD_REQUEST
        )

    WeatherModel.objects.filter(id=pk).update(
        is_active=False,
        is_deleted=True
    )

    return Response(
        {"message": "Weather type deleted successfully"},
        status=HTTP_200_OK,
    )


@api_view(["PATCH"])
def deactivate_weather_type(request, pk):
    if not WeatherModel.objects.filter(id=pk).exists():
        return Response(
            {"error": "Weather type does not exists"}, status=HTTP_400_BAD_REQUEST
        )

    WeatherModel.objects.filter(id=pk).update(
        is_active=False,
    )

    return Response(
        {"message": "Weather type deactivated successfully"},
        status=HTTP_200_OK,
    )


@api_view(["PATCH"])
def activate_weather_type(request, pk):
    if not WeatherModel.objects.filter(id=pk).exists():
        return Response(
            {"error": "Weather type does not exists"}, status=HTTP_400_BAD_REQUEST
        )

    WeatherModel.objects.filter(id=pk).update(
        is_active=True,
    )

    return Response(
        {"message": "Weather type activated successfully"},
        status=HTTP_200_OK,
    )


@api_view(["GET"])
def get_all_weather_types(request):
    weathers = WeatherModel.objects.all()

    serializer = WeatherSerializer(weathers, many=True)

    return Response(serializer.data, status=HTTP_200_OK)


@api_view(["GET"])
def get_all_active_weather_types(request):
    weathers = WeatherModel.objects.filter(is_active=True, is_deleted=False)

    serializer = WeatherSerializer(weathers, many=True)

    return Response(serializer.data, status=HTTP_200_OK)


@api_view(["GET"])
def get_weather_type_by_id(request, pk):
    try:
        weather = WeatherModel.objects.get(id=pk, is_active=True, is_deleted=False)
    except WeatherModel.DoesNotExist:
        return Response(
            {"error": "Weather type does not exists"}, status=HTTP_400_BAD_REQUEST
        )

    serializer = WeatherSerializer(weather)

    return Response(serializer.data, status=HTTP_200_OK)
