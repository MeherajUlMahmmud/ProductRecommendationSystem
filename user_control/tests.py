from rest_framework.test import APITestCase

from user_control.models import UserModel
from user_control.serializer import UserSerializer


class TestUserModel(APITestCase):

    def setUp(self):
        # Creating a customer type user
        self.customer = UserModel.objects.create_customer(
            email='testcustomer@gmail.com', name='Test Customer', password='asdf123ASDF')
        # Creating a vendor type user
        self.vendor = UserModel.objects.create_vendor(
            email='testvendor@gmail.com', name='Test Vendor', password='asdf123ASDF')
        # Creating an admin type user
        self.admin = UserModel.objects.create_admin(
            email='testadmin@gmail.com', name='Test Admin', password='asdf123ASDF')

    # Test for customer's email
    def test_customer_email(self):
        expected_object_email = self.customer.email
        self.assertEquals(expected_object_email, 'testcustomer@gmail.com')

    # Test for vendor's email
    def test_vendor_email(self):
        expected_object_email = self.vendor.email
        self.assertEquals(expected_object_email, 'testvendor@gmail.com')

    # Test for admin's email
    def test_admin_email(self):
        expected_object_email = self.admin.email
        self.assertEquals(expected_object_email, 'testadmin@gmail.com')

    # Test for customer's name
    def test_customer_name(self):
        expected_object_name = self.customer.name
        self.assertEquals(expected_object_name, 'Test Customer')

    # Test for vendor's name
    def test_vendor_name(self):
        expected_object_name = self.vendor.name
        self.assertEquals(expected_object_name, 'Test Vendor')

    # Test for admin's name
    def test_admin_name(self):
        expected_object_name = self.admin.name
        self.assertEquals(expected_object_name, 'Test Admin')

    def test_customer_is_customer(self):
        expected_object_is_customer = self.customer.is_customer
        self.assertEquals(expected_object_is_customer, True)

    def test_vendor_is_vendor(self):
        expected_object_is_vendor = self.vendor.is_vendor
        self.assertEquals(expected_object_is_vendor, True)

    def test_admin_is_admin(self):
        expected_object_is_admin = self.admin.is_admin
        self.assertEquals(expected_object_is_admin, True)

    def test_login_success(self):
        response = self.client.login(email='testadmin@gmail.com', password='asdf123ASDF')
        self.assertTrue(response)

    def test_login_fail(self):
        response = self.client.login(email='testadmin@gmail.com', password='asdf')
        self.assertFalse(response)

    # Deleting previously created user type object
    def tearDown(self):
        self.customer.delete()
        self.vendor.delete()
        self.admin.delete()


class TestUserSerializer(APITestCase):

    def setUp(self):
        # Creating a customer type user
        self.customer = UserModel.objects.create_customer(
            email='testcustomer@gmail.com', name='Test Customer', password='asdf123ASDF')
        # Creating a vendor type user
        self.vendor = UserModel.objects.create_vendor(
            email='testvendor@gmail.com', name='Test Vendor', password='asdf123ASDF')
        # Creating an admin type user
        self.admin = UserModel.objects.create_admin(
            email='testadmin@gmail.com', name='Test Admin', password='asdf123ASDF')

        # Creating a customer type user serializer
        self.customer_serializer = UserSerializer(self.customer)
        # Creating a vendor type user serializer
        self.vendor_serializer = UserSerializer(self.vendor)
        # Creating an admin type user serializer
        self.admin_serializer = UserSerializer(self.admin)

    # Test for customer's email
    def test_customer_email(self):
        expected_object_email = self.customer_serializer.data['email']
        self.assertEquals(expected_object_email, 'testcustomer@gmail.com')

    # Test for vendor's email
    def test_vendor_email(self):
        expected_object_email = self.vendor_serializer.data['email']
        self.assertEquals(expected_object_email, 'testvendor@gmail.com')

    # Test for admin's email
    def test_admin_email(self):
        expected_object_email = self.admin_serializer.data['email']
        self.assertEquals(expected_object_email, 'testadmin@gmail.com')

    # Test for customer's name
    def test_customer_name(self):
        expected_object_name = self.customer_serializer.data['name']
        self.assertEquals(expected_object_name, 'Test Customer')

    # Test for vendor's name
    def test_vendor_name(self):
        expected_object_name = self.vendor_serializer.data['name']
        self.assertEquals(expected_object_name, 'Test Vendor')

    # Test for admin's name
    def test_admin_name(self):
        expected_object_name = self.admin_serializer.data['name']
        self.assertEquals(expected_object_name, 'Test Admin')

    # Test for customer's is_customer
    def test_customer_is_customer(self):
        expected_object_is_customer = self.customer_serializer.data['is_customer']
        self.assertEquals(expected_object_is_customer, True)

    # Test for vendor's is_vendor
    def test_vendor_is_vendor(self):
        expected_object_is_vendor = self.vendor_serializer.data['is_vendor']
        self.assertEquals(expected_object_is_vendor, True)

    # Test for admin's is_admin
    def test_admin_is_admin(self):
        expected_object_is_admin = self.admin_serializer.data['is_admin']
        self.assertEquals(expected_object_is_admin, True)

    # Deleting previously created user type object
    def tearDown(self):
        self.customer.delete()
        self.vendor.delete()
        self.admin.delete()


class TestUserViewSet(APITestCase):

    def setUp(self):
        # Creating a customer type user
        self.customer = UserModel.objects.create_customer(
            email='testcustomer@gmail.com', name='Test Customer', password='asdf123ASDF')
        # Creating a vendor type user
        self.vendor = UserModel.objects.create_vendor(
            email='testvendor@gmail.com', name='Test Vendor', password='asdf123ASDF')
        # Creating an admin type user
        self.admin = UserModel.objects.create_admin(
            email='testadmin@gmail.com', name='Test Admin', password='asdf123ASDF')
