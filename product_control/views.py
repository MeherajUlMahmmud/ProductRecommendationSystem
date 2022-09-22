from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK

from product_control.models import ProductTypeModel
from product_control.serializer import ProductTypeSerializer
from user_control.decorators import admin_only


@api_view(["POST"])
@admin_only()
def create_new_product_type(request):
    print(request.data)
    data = request.data
    product_type = data.get("product_type")

    if not product_type:
        return Response({"error": "Product Type is required"}, status=HTTP_400_BAD_REQUEST)

    if len(product_type) > 50:
        return Response({"error": "Product Type must be less than 50 characters"}, status=HTTP_400_BAD_REQUEST)

    product = ProductTypeModel.objects.create(
        product_type=product_type
    )
    product.save()

    return Response(
        {"message": "Product Type created successfully"},
        status=HTTP_201_CREATED,
    )


@api_view(["PATCH"])
@admin_only()
def update_product_type(request, pk):
    print(request.data)
    data = request.data
    product_type = data.get("product_type")

    if not product_type:
        return Response({"error": "Product Type is required"}, status=HTTP_400_BAD_REQUEST)

    if len(product_type) > 50:
        return Response({"error": "Product Type must be less than 50 characters"}, status=HTTP_400_BAD_REQUEST)

    if not ProductTypeModel.objects.filter(id=pk).exists():
        return Response({"error": "Product Type does not exist"}, status=HTTP_400_BAD_REQUEST)

    product = ProductTypeModel.objects.get(id=pk)
    product.product_type = product_type
    product.save()

    return Response(
        {"message": "Product Type updated successfully"},
        status=HTTP_201_CREATED,
    )


@api_view(["DELETE"])
@admin_only()
def delete_product_type(request, pk):
    if not ProductTypeModel.objects.filter(id=pk).exists():
        return Response({"error": "Product Type does not exist"}, status=HTTP_400_BAD_REQUEST)

    product = ProductTypeModel.objects.get(id=pk)
    product.is_deleted = True
    product.save()

    return Response(
        {"message": "Product Type deleted successfully"},
        status=HTTP_201_CREATED,
    )


@api_view(["PATCH"])
@admin_only()
def restore_product_type(request, pk):
    if not ProductTypeModel.objects.filter(id=pk).exists():
        return Response({"error": "Product Type does not exist"}, status=HTTP_400_BAD_REQUEST)

    product = ProductTypeModel.objects.get(id=pk)
    product.is_deleted = False
    product.save()

    return Response(
        {"message": "Product Type restored successfully"},
        status=HTTP_200_OK,
    )


@api_view(["PATCH"])
@admin_only()
def activate_product_type(request, pk):
    if not ProductTypeModel.objects.filter(id=pk).exists():
        return Response({"error": "Product Type does not exist"}, status=HTTP_400_BAD_REQUEST)

    product = ProductTypeModel.objects.get(id=pk)
    product.is_active = True
    product.save()

    return Response(
        {"message": "Product Type activated successfully"},
        status=HTTP_200_OK,
    )


@api_view(["PATCH"])
@admin_only()
def deactivate_product_type(request, pk):
    if not ProductTypeModel.objects.filter(id=pk).exists():
        return Response({"error": "Product Type does not exist"}, status=HTTP_400_BAD_REQUEST)

    product = ProductTypeModel.objects.get(id=pk)
    product.is_active = False
    product.save()

    return Response(
        {"message": "Product Type deactivated successfully"},
        status=HTTP_200_OK,
    )


@api_view(["GET"])
@admin_only()
def get_all_product_types(request):
    products = ProductTypeModel.objects.all()
    serializer = ProductTypeSerializer(products, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(["GET"])
@admin_only()
def get_all_active_product_types(request):
    products = ProductTypeModel.objects.filter(is_active=True)
    serializer = ProductTypeSerializer(products, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(["GET"])
@admin_only()
def get_product_type(request, pk):
    try:
        product = ProductTypeModel.objects.get(id=pk, is_active=True, is_deleted=False)
    except ProductTypeModel.DoesNotExist:
        return Response(
            {"error": "Product Type does not exists"}, status=HTTP_400_BAD_REQUEST
        )

    serializer = ProductTypeSerializer(product)
    return Response(serializer.data, status=HTTP_200_OK)
