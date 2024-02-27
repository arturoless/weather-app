import unittest
from main import app

TEST_CITY = 'monterrey'


class TestWeatherAPI(unittest.TestCase):

    def test_get_weather_success(self):
        """
        Test that the /weather/<city> endpoint returns valid data for a valid city.
        """
        with app.test_client() as client:
            response = client.get(f'/weather/{TEST_CITY}')
            self.assertEqual(response.status_code, 200)
            data = response.json
            self.assertIsNotNone(data)
            self.assertIn('city', data)
            self.assertIn('forecast', data)
            self.assertEqual(data['city'], f"{TEST_CITY}")
            self.assertGreaterEqual(len(data['forecast']), 1)
            self.assertIn('date', data['forecast'][0])
            self.assertIn('max_temp', data['forecast'][0])
            self.assertIn('min_temp', data['forecast'][0])
            self.assertIn('weather', data['forecast'][0])


    def test_get_weather_invalid_city(self):
        """
        Test that the /weather/<city> endpoint returns a 404 for an invalid city.
        """
        with app.test_client() as client:
            response = client.get('/weather/NonexistentCity')
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json, {'error': 'City not found'})


    def test_api_endpoint_success(self):
        """
        Test that the /weather/<city> endpoint returns a successful response.
        """
        with app.test_client() as client:
            response = client.get(f'/weather/{TEST_CITY}')
            self.assertEqual(response.status_code, 200)
            data = response.json
            self.assertIsNotNone(data)
            # Assert similar structure as in test_get_weather_data_success

    def test_api_endpoint_invalid_city(self):
        """
        Test that the /weather/<city> endpoint returns a 404 for an invalid city.
        """
        with app.test_client() as client:
            response = client.get('/weather/NonexistentCity')
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json, {'error': 'City not found'})


if __name__ == '__main__':
    unittest.main()
