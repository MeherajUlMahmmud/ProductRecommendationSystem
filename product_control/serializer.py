from rest_framework import serializers

from product_control.models import ProductTypeModel, ProductModel


class ProductTypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ProductTypeModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    product_type = ProductTypeSerializer()

    class Meta:
        model = ProductModel
        fields = '__all__'
