from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

from user_control.models import UserModel
from user_control.utils import verify_token


def admin_only():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            token = request.COOKIES.get("x-auth-token")

            if not token:
                return Response({"message": "Authorization denied"}, status=HTTP_401_UNAUTHORIZED)

            user_id = verify_token(token)
            user = UserModel.objects.get(id=user_id)

            if not user.is_admin:
                return Response({"message": "Authorization denied"}, status=HTTP_401_UNAUTHORIZED)
            else:
                return view_func(request, *args, **kwargs)

        return wrapper_func

    return decorator


def vendor_only():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            token = request.COOKIES.get("x-auth-token")

            if not token:
                return Response({"message": "Authorization denied"}, status=HTTP_401_UNAUTHORIZED)

            user_id = verify_token(token)
            user = UserModel.objects.get(id=user_id)

            if not user.is_vendor:
                return Response({"message": "Authorization denied"}, status=HTTP_401_UNAUTHORIZED)
            else:
                return view_func(request, *args, **kwargs)

        return wrapper_func

    return decorator
