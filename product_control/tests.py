from rest_framework.test import APITestCase

from product_control.models import ProductTypeModel, ProductModel
from user_control.models import UserModel


class TestProductTypeModel(APITestCase):

    def setUp(self):
        self.product_type = ProductTypeModel.objects.create(product_type='Normal')

    def test_product_type(self):
        expected_object_product_type = self.product_type.product_type
        self.assertEquals(expected_object_product_type, 'Normal')

    def test_product_type_update(self):
        self.product_type.product_type = 'Hot'
        self.product_type.save()
        expected_object_product_type = self.product_type.product_type
        self.assertEquals(expected_object_product_type, 'Hot')

    def test_product_type_delete(self):
        self.product_type.is_deleted = True
        expected_object_product_type_status = self.product_type.is_deleted
        self.assertTrue(expected_object_product_type_status)

    def test_product_type_restore(self):
        self.product_type.is_deleted = False
        expected_object_product_type_status = self.product_type.is_deleted
        self.assertFalse(expected_object_product_type_status)

    def test_product_type_deactivate(self):
        self.product_type.is_active = False
        expected_object_product_type_status = self.product_type.is_active
        self.assertFalse(expected_object_product_type_status)

    def test_product_type_activate(self):
        self.product_type.is_active = True
        expected_object_product_type_status = self.product_type.is_active
        self.assertTrue(expected_object_product_type_status)

    def tearDown(self):
        self.product_type.delete()


class TestProductModel(APITestCase):

    def setUp(self):
        self.vendor = UserModel.objects.create_vendor(
            email='testvendor@gmail.com', name='Test Vendor', password='asdf123ASDF')

        self.product_type_1 = ProductTypeModel.objects.create(product_type='Normal')
        self.product_type_2 = ProductTypeModel.objects.create(product_type='Hot')
        self.product = ProductModel.objects.create(
            vendor=self.vendor,
            product_type=self.product_type_1,
            product_name='Normal Product',
            product_description='This is a normal product',
            available_quantity=10,
            unit_price=1000,
        )

    def test_product_type(self):
        expected_object_product_type = self.product.product_type
        self.assertEquals(expected_object_product_type, self.product_type_1)

    def test_product_name(self):
        expected_object_product_name = self.product.product_name
        self.assertEquals(expected_object_product_name, 'Normal Product')

    def test_product_description(self):
        expected_object_product_description = self.product.product_description
        self.assertEquals(expected_object_product_description, 'This is a normal product')

    def test_product_price(self):
        expected_object_product_price = self.product.unit_price
        self.assertEquals(expected_object_product_price, 1000)

    def test_product_type_update(self):
        self.product.product_type = self.product_type_2
        self.product.save()
        expected_object_product_type = self.product.product_type
        self.assertEquals(expected_object_product_type, self.product_type_2)

    def test_product_name_update(self):
        self.product.product_name = 'Hot Product'
        self.product.save()
        expected_object_product_name = self.product.product_name
        self.assertEquals(expected_object_product_name, 'Hot Product')

    def test_product_description_update(self):
        self.product.product_description = 'This is a hot product'
        self.product.save()
        expected_object_product_description = self.product.product_description
        self.assertEquals(expected_object_product_description, 'This is a hot product')

    def test_product_price_update(self):
        self.product.unit_price = 2000
        self.product.save()
        expected_object_product_price = self.product.unit_price
        self.assertEquals(expected_object_product_price, 2000)

    def test_product_type_delete(self):
        self.product.is_deleted = True
        expected_object_product_type_status = self.product.is_deleted
        self.assertTrue(expected_object_product_type_status)

    def test_product_type_restore(self):
        self.product.is_deleted = False
        expected_object_product_type_status = self.product.is_deleted
        self.assertFalse(expected_object_product_type_status)

    def test_product_type_deactivate(self):
        self.product.is_active = False
        expected_object_product_type_status = self.product.is_active
        self.assertFalse(expected_object_product_type_status)

    def test_product_type_activate(self):
        self.product.is_active = True
        expected_object_product_type_status = self.product.is_active
        self.assertTrue(expected_object_product_type_status)

    def tearDown(self):
        self.vendor.delete()
        self.product_type_1.delete()
        self.product_type_2.delete()
        self.product.delete()
