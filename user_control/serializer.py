from rest_framework import serializers

from user_control.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserModel
        fields = ("id", "name", "email", "address", "is_customer", "is_vendor", "is_admin")


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'name', 'address')
