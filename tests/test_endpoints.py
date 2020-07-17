import unittest
import requests


BASE_URL = 'http://127.0.0.1:5000'


class TestApi(unittest.TestCase):

    def test_users(self):
        response = requests.get(BASE_URL+'/users')
        assert response.status_code == 200

    def test_user_page(self):
        response = requests.get(BASE_URL+'/users/charlidamelio')
        assert response.status_code == 200

    def test_top_country(self):
        response = requests.get(BASE_URL+'/top/country/us')
        assert response.status_code == 200

    def test_error_page(self):
        response = requests.get(BASE_URL+'/not/found')
        assert response.status_code == 404
