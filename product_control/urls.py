from django.urls import path

from product_control.views import (create_new_product_type, update_product_type, delete_product_type,
                                   activate_product_type, deactivate_product_type, get_all_product_types,
                                   get_product_type, get_all_active_product_types)

urlpatterns = [
    path("create", create_new_product_type),
    path("update/<str:pk>", update_product_type),
    path("delete/<str:pk>", delete_product_type),
    path("activate/<str:pk>", activate_product_type),
    path("deactivate/<str:pk>", deactivate_product_type),
    path("list", get_all_product_types),
    path("list/active", get_all_active_product_types),
    path("<str:pk>", get_product_type),
]
