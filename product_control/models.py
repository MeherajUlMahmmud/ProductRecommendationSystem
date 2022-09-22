from django.db import models


class ProductTypeModel(models.Model):
    product_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_type

    class Meta:
        verbose_name = 'Product Type'
        verbose_name_plural = 'Product Types'


class ProductModel(models.Model):
    product_type = models.ForeignKey(ProductTypeModel, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(null=True, blank=True)
    available_quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
