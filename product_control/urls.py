from django.urls import path

from product_control.views import (create_new_product_type, update_product_type, delete_product_type,
                                   activate_product_type, deactivate_product_type, get_all_product_types,
                                   get_product_type, get_all_active_product_types, restore_product_type)

urlpatterns = [
    path("type/create", create_new_product_type),
    path("type/update/<str:pk>", update_product_type),
    path("type/delete/<str:pk>", delete_product_type),
    path("type/restore/<str:pk>", restore_product_type),
    path("type/activate/<str:pk>", activate_product_type),
    path("type/deactivate/<str:pk>", deactivate_product_type),
    path("type/list", get_all_product_types),
    path("type/list/active", get_all_active_product_types),
    path("type/<str:pk>", get_product_type),
]
