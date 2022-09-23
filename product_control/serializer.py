from rest_framework import serializers

from product_control.models import ProductTypeModel, ProductModel
from user_control.serializer import UserSerializer, VendorSerializer


class ProductTypeAdminSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ProductTypeModel
        fields = '__all__'


class ProductTypeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTypeModel
        fields = ('id', 'product_type')


class ProductAdminSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    product_type = ProductTypeAdminSerializer()
    vendor = UserSerializer(read_only=True)

    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    product_type = ProductTypeUserSerializer()
    vendor = VendorSerializer(read_only=True)

    class Meta:
        model = ProductModel
        fields = (
            'id', 'product_name', 'product_description', 'product_type', 'vendor', 'unit_price', 'available_quantity',)
