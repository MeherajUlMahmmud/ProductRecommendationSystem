from rest_framework import serializers

from user_control.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    email = serializers.CharField()
    address = serializers.CharField()
    is_customer = serializers.BooleanField()
    is_vendor = serializers.BooleanField()
    is_admin = serializers.BooleanField()

    class Meta:
        model = UserModel
        fields = ("id", "name", "email", "address", "is_customer", "is_vendor", "is_admin")
