from django.contrib import admin

from .models import ProductTypeModel, ProductModel

admin.site.register(ProductTypeModel)
admin.site.register(ProductModel)
