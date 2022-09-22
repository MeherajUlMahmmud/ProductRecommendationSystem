from django.urls import path

from user_control.views import (
    login_view, customer_signup_view, vendor_signup_view, admin_signup_view,
)

urlpatterns = [
    path("login", login_view),
    path("signup", customer_signup_view),
    path("vendor/signup", vendor_signup_view),
    path("admin/signup", admin_signup_view),
]
