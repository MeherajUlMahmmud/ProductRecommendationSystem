import os

import requests
from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK

from product_control.models import ProductModel, ProductTypeModel
from product_control.serializer import ProductSerializer
from user_control.decorators import admin_only
from weather_control.models import WeatherModel

load_dotenv()


@api_view(["POST"])
@admin_only()
def create_new_product(request):
    print(request.data)
    data = request.data
    product_type_id = data.get("product_type_id")
    product_name = data.get("product_name")
    product_description = data.get("product_description")
    available_quantity = data.get("available_quantity")
    unit_price = data.get("unit_price")

    if not product_type_id:
        return Response({"error": "Product Type is required"}, status=HTTP_400_BAD_REQUEST)

    if not product_name:
        return Response({"error": "Product Name is required"}, status=HTTP_400_BAD_REQUEST)

    if not available_quantity:
        return Response({"error": "Available Quantity is required"}, status=HTTP_400_BAD_REQUEST)

    if not unit_price:
        return Response({"error": "Unit Price is required"}, status=HTTP_400_BAD_REQUEST)

    if len(product_name) > 50:
        return Response({"error": "Product Name must be less than 50 characters"}, status=HTTP_400_BAD_REQUEST)

    if type(available_quantity) != int:
        return Response({"error": "Available Quantity must be an integer"}, status=HTTP_400_BAD_REQUEST)

    if available_quantity < 0:
        return Response({"error": "Available Quantity must be greater than 0"}, status=HTTP_400_BAD_REQUEST)

    if type(unit_price) != int and type(unit_price) != float:
        return Response({"error": "Unit Price must be a number"}, status=HTTP_400_BAD_REQUEST)

    if unit_price < 0:
        return Response({"error": "Unit Price must be greater than 0"}, status=HTTP_400_BAD_REQUEST)

    try:
        product_type = ProductTypeModel.objects.get(id=product_type_id)
    except ProductTypeModel.DoesNotExist:
        return Response({"error": "Product Type does not exist"}, status=HTTP_400_BAD_REQUEST)

    product = ProductModel.objects.create(
        product_type=product_type,
        product_name=product_name,
        product_description=product_description,
        available_quantity=available_quantity,
        unit_price=unit_price
    )
    product.save()

    return Response(
        {"message": "Product created successfully"},
        status=HTTP_201_CREATED,
    )


@api_view(["PATCH"])
@admin_only()
def update_product(request, pk):
    print(request.data)
    data = request.data
    product_type_id = data.get("product_type_id")
    product_name = data.get("product_name")
    product_description = data.get("product_description")
    available_quantity = data.get("available_quantity")
    unit_price = data.get("unit_price")

    if not product_type_id:
        return Response({"error": "Product Type is required"}, status=HTTP_400_BAD_REQUEST)

    if not product_name:
        return Response({"error": "Product Name is required"}, status=HTTP_400_BAD_REQUEST)

    if not available_quantity:
        return Response({"error": "Available Quantity is required"}, status=HTTP_400_BAD_REQUEST)

    if not unit_price:
        return Response({"error": "Unit Price is required"}, status=HTTP_400_BAD_REQUEST)

    if len(product_name) > 50:
        return Response({"error": "Product Name must be less than 50 characters"}, status=HTTP_400_BAD_REQUEST)

    if available_quantity < 0:
        return Response({"error": "Available Quantity must be greater than 0"}, status=HTTP_400_BAD_REQUEST)

    if unit_price < 0:
        return Response({"error": "Unit Price must be greater than 0"}, status=HTTP_400_BAD_REQUEST)

    try:
        product_type = ProductTypeModel.objects.get(id=product_type_id)
    except ProductTypeModel.DoesNotExist:
        return Response({"error": "Product Type does not exist"}, status=HTTP_400_BAD_REQUEST)

    product = ProductModel.objects.get(id=pk)
    product.product_type = product_type
    product.product_name = product_name
    product.product_description = product_description
    product.available_quantity = available_quantity
    product.unit_price = unit_price
    product.save()

    return Response(
        {"message": "Product updated successfully"},
        status=HTTP_200_OK,
    )


@api_view(["DELETE"])
@admin_only()
def delete_product(request, pk):
    if not ProductModel.objects.filter(id=pk).exists():
        return Response({"error": "Product does not exist"}, status=HTTP_400_BAD_REQUEST)

    product = ProductModel.objects.get(id=pk)
    product.is_deleted = True
    product.save()

    return Response(
        {"message": "Product deleted successfully"},
        status=HTTP_200_OK,
    )


@api_view(["PATCH"])
@admin_only()
def restore_product(request, pk):
    if not ProductModel.objects.filter(id=pk).exists():
        return Response({"error": "Product does not exist"}, status=HTTP_400_BAD_REQUEST)

    product = ProductModel.objects.get(id=pk)
    product.is_deleted = False
    product.save()

    return Response(
        {"message": "Product restored successfully"},
        status=HTTP_200_OK,
    )


@api_view(["PATCH"])
@admin_only()
def activate_product(request, pk):
    if not ProductModel.objects.filter(id=pk).exists():
        return Response({"error": "Product does not exist"}, status=HTTP_400_BAD_REQUEST)

    product = ProductModel.objects.get(id=pk)
    product.is_active = True
    product.save()

    return Response(
        {"message": "Product activated successfully"},
        status=HTTP_200_OK,
    )


@api_view(["PATCH"])
@admin_only()
def deactivate_product(request, pk):
    if not ProductModel.objects.filter(id=pk).exists():
        return Response({"error": "Product does not exist"}, status=HTTP_400_BAD_REQUEST)

    product = ProductModel.objects.get(id=pk)
    product.is_active = False
    product.save()

    return Response(
        {"message": "Product deactivated successfully"},
        status=HTTP_200_OK,
    )


@api_view(["GET"])
@admin_only()
def get_all_products(request):
    products = ProductModel.objects.filter(is_active=True, is_deleted=False)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(["GET"])
def get_all_active_products(request):
    products = ProductModel.objects.filter(is_active=True, is_deleted=False)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(["GET"])
def get_all_active_products_by_type(request, product_type):
    products = ProductModel.objects.filter(is_active=True, is_deleted=False,
                                           product_type__product_type__contains=product_type)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(["GET"])
def get_all_active_products_by_name(request, product_name):
    products = ProductModel.objects.filter(is_active=True, is_deleted=False, product_name__icontains=product_name)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(["GET"])
def get_product_by_id(request, pk):
    if not ProductModel.objects.filter(id=pk).exists():
        return Response({"error": "Product does not exist"}, status=HTTP_400_BAD_REQUEST)

    product = ProductModel.objects.get(id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(["GET"])
def get_recommended_product(request):
    # get weather data from open weather api
    res = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=Dhaka&appid=" + os.getenv("OPEN_WEATHER_API_KEY")
    )
    if res.status_code != 200:
        return Response({"error": "Error getting weather data"}, status=HTTP_400_BAD_REQUEST)

    weather_data = res.json()
    temperature = weather_data['main']['temp']  # extract temperature from weather data
    temperature = temperature - 273.15  # convert kelvin to celsius
    temperature = round(temperature, 2)  # round to 2 decimal places

    try:
        weather_type = WeatherModel.objects.get(
            min_temp__lte=temperature,
            max_temp__gte=temperature
        )
    except WeatherModel.DoesNotExist:
        return Response({"error": "Suitable Weather Type could not be found"}, status=HTTP_400_BAD_REQUEST)

    try:
        product_type = ProductTypeModel.objects.get(product_type__contains=weather_type.weather_type)
    except ProductTypeModel.DoesNotExist:
        return Response({"error": "Product Type could not be found"}, status=HTTP_400_BAD_REQUEST)

    products = ProductModel.objects.filter(is_active=True, is_deleted=False, product_type=product_type)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=HTTP_200_OK)
