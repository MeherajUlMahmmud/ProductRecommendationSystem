from rest_framework import serializers

from product_control.models import ProductTypeModel


class ProductTypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    product_type = serializers.CharField()
    is_active = serializers.BooleanField()
    is_deleted = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = ProductTypeModel
        fields = '__all__'
