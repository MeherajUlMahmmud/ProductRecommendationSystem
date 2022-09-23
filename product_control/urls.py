from django.urls import path

from product_control.views.product_type_views import (create_new_product_type, update_product_type, delete_product_type,
                                                      activate_product_type, deactivate_product_type,
                                                      get_all_product_types,
                                                      get_product_type, get_all_active_product_types,
                                                      restore_product_type)
from product_control.views.product_views import create_new_product, update_product, delete_product, restore_product, \
    activate_product, deactivate_product, get_all_products, get_all_active_products, get_all_active_products_by_type, \
    get_all_active_products_by_name, get_product_by_id, get_recommended_product

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

    path("create", create_new_product),
    path("update/<str:pk>", update_product),
    path("delete/<str:pk>", delete_product),
    path("restore/<str:pk>", restore_product),
    path("activate/<str:pk>", activate_product),
    path("deactivate/<str:pk>", deactivate_product),
    path("list", get_all_products),
    path("list/active", get_all_active_products),
    path("list/active/type/<str:product_type>", get_all_active_products_by_type),
    path("list/active/name/<str:product_name>", get_all_active_products_by_name),
    path("<str:pk>", get_product_by_id),
    path("list/recommended", get_recommended_product),
]
