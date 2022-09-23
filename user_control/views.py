import os

from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.exceptions import (
    AuthenticationFailed,
)
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)

from user_control.models import UserModel
from user_control.utils import create_token
from .serializer import UserSerializer

load_dotenv()


@api_view(["POST"])
def customer_signup_view(request):
    print(request.data)
    data = request.data

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name:
        return Response({"error": "Name is required"}, status=HTTP_400_BAD_REQUEST)

    if not email:
        return Response({"error": "Email address is required"}, status=HTTP_400_BAD_REQUEST)

    if not password:
        return Response({"error": "Password is required"}, status=HTTP_400_BAD_REQUEST)

    if password and len(password) < 6:
        return Response({"error": "Password must be at least 6 characters"}, status=HTTP_400_BAD_REQUEST)

    if UserModel.objects.filter(email=email).exists():
        return Response(
            {"error": "Email address already exists"}, status=HTTP_400_BAD_REQUEST
        )

    user = UserModel.objects.create_customer(
        name=name, email=email, password=password
    )
    user.save()

    return Response(
        {"message": "User created successfully"},
        status=HTTP_201_CREATED,
    )


@api_view(["POST"])
def vendor_signup_view(request):
    print(request.data)
    data = request.data

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name:
        return Response({"error": "Name is required"}, status=HTTP_400_BAD_REQUEST)

    if not email:
        return Response({"error": "Email address is required"}, status=HTTP_400_BAD_REQUEST)

    if not password:
        return Response({"error": "Password is required"}, status=HTTP_400_BAD_REQUEST)

    if password and len(password) < 6:
        return Response({"error": "Password must be at least 6 characters"}, status=HTTP_400_BAD_REQUEST)

    if UserModel.objects.filter(email=email).exists():
        return Response(
            {"error": "Email address already exists"}, status=HTTP_400_BAD_REQUEST
        )

    user = UserModel.objects.create_vendor(
        name=name, email=email, password=password
    )
    user.save()

    return Response(
        {"message": "Vendor created successfully"},
        status=HTTP_201_CREATED,
    )


@api_view(["POST"])
def admin_signup_view(request):
    print(request.data)
    data = request.data

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    authorization_code = data.get("authorization_code")

    if not name:
        return Response({"error": "Name is required"}, status=HTTP_400_BAD_REQUEST)

    if not email:
        return Response({"error": "Email address is required"}, status=HTTP_400_BAD_REQUEST)

    if not password:
        return Response({"error": "Password is required"}, status=HTTP_400_BAD_REQUEST)

    if password and len(password) < 6:
        return Response({"error": "Password must be at least 6 characters"}, status=HTTP_400_BAD_REQUEST)

    # fetch authorization_code from env
    if authorization_code != os.getenv("AUTHORIZATION_CODE"):
        return Response(
            {"error": "Invalid access"}, status=HTTP_400_BAD_REQUEST
        )

    if UserModel.objects.filter(email=email).exists():
        return Response(
            {"error": "Email address already exists"}, status=HTTP_400_BAD_REQUEST
        )

    user = UserModel.objects.create_admin(
        name=name, email=email, password=password
    )
    user.save()

    return Response(
        {"message": "Admin created successfully"},
        status=HTTP_201_CREATED,
    )


@api_view(["POST"])
def login_view(request):
    print(request.data)
    data = request.data
    email = data.get("email")
    password = data.get("password")

    try:
        user = UserModel.objects.get(email=email)
    except UserModel.DoesNotExist:
        raise AuthenticationFailed("User not found")

    if not user.check_password(password):
        print("Incorrect password")
        raise AuthenticationFailed("Incorrect password")
    if not user.is_active:
        print("User is not active")
        raise AuthenticationFailed("Account disabled")
    if not user.is_verified:
        raise AuthenticationFailed("Account is not verified")

    print("User logged in")
    token = create_token(user)

    data = UserSerializer(user).data

    res = Response({"message": "Login successful", "user": data})
    res.set_cookie(key="x-auth-token", value=token, httponly=True)

    return res


@api_view(["POST"])
def logout_view(request):
    res = Response({"message": "Logout successful"})
    res.delete_cookie(key="x-auth-token")
    return res
