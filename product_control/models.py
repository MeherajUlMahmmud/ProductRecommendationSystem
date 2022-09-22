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
