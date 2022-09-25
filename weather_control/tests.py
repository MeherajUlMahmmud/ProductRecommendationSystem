from rest_framework.test import APITestCase

from weather_control.models import WeatherModel


class TestWeatherModel(APITestCase):

    def setUp(self):
        # self.factory = APIRequestFactory()

        self.cold_weather = WeatherModel.objects.create(
            weather_type="Cold",
            min_temp=-5,
            max_temp=20,
        )
        self.hot_weather = WeatherModel.objects.create(
            weather_type="Hot",
            min_temp=27,
            max_temp=40,
        )
        self.normal_weather = WeatherModel.objects.create(
            weather_type="Normal",
            min_temp=21,
            max_temp=26,
        )

    def test_weather_type(self):
        expected_object_weather_type = self.cold_weather.weather_type
        self.assertEquals(expected_object_weather_type, "Cold")

    def test_min_temp(self):
        expected_object_min_temp = self.hot_weather.min_temp
        self.assertEquals(expected_object_min_temp, 27)

    def test_max_temp(self):
        expected_object_max_temp = self.normal_weather.max_temp
        self.assertEquals(expected_object_max_temp, 26)

    def test_weather_type_update(self):
        self.cold_weather.weather_type = "Freezing"
        self.cold_weather.save()
        expected_object_weather_type = self.cold_weather.weather_type
        self.assertEquals(expected_object_weather_type, "Freezing")

    def test_min_temp_update(self):
        self.hot_weather.min_temp = 30
        self.hot_weather.save()
        expected_object_min_temp = self.hot_weather.min_temp
        self.assertEquals(expected_object_min_temp, 30)

    def test_max_temp_update(self):
        self.normal_weather.max_temp = 29
        self.normal_weather.save()
        expected_object_max_temp = self.normal_weather.max_temp
        self.assertEquals(expected_object_max_temp, 29)

    def test_weather_type_delete(self):
        self.cold_weather.is_deleted = True
        expected_object_weather_type_status = self.cold_weather.is_deleted
        self.assertTrue(expected_object_weather_type_status)

    def test_weather_type_restore(self):
        self.cold_weather.is_deleted = False
        expected_object_weather_type_status = self.cold_weather.is_deleted
        self.assertFalse(expected_object_weather_type_status)

    def test_weather_type_deactivate(self):
        self.cold_weather.is_active = False
        expected_object_weather_type_status = self.cold_weather.is_active
        self.assertFalse(expected_object_weather_type_status)

    def test_weather_type_activate(self):
        self.cold_weather.is_active = True
        expected_object_weather_type_status = self.cold_weather.is_active
        self.assertTrue(expected_object_weather_type_status)

    def tearDown(self):
        self.cold_weather.delete()
        self.hot_weather.delete()
        self.normal_weather.delete()

    # def authenticate(self):
    #     sample_login_data = {
    #         "email": "testadmin@gmail.com",
    #         "password": "asdf123ASDF"
    #     }
    #     request = self.factory.post("api/auth/login", sample_login_data)
    #     response = login_view(request)
    #     self.factory.cookies = response.cookies  # set the cookie to the factory
    #
    # def test_should_not_create_weather_type(self):
    #     sample_weather = {
    #         "weather_type": "London",
    #         "min_temp": 10,
    #         "max_temp": 20,
    #     }
    #
    #     request = self.factory.post("api/weather/create", sample_weather)
    #     response = create_new_weather_type(request)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #
    # def test_should_create_weather_type(self):
    #     sample_weather = {
    #         "weather_type": "London",
    #         "min_temp": 10,
    #         "max_temp": 20,
    #     }
    #
    #     self.authenticate()
    #     request = self.factory.post("api/weather/create", sample_weather)
    #     response = create_new_weather_type(request)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
