import unittest
import json

from models import app


BASE_URL = 'http://127.0.0.1:5000'
USERS = '{}/users'.format(BASE_URL)


class TestApi(unittest.TestCase):

    def test_get_users(self):
        response = app.get(USERS)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['users_list']), 200)

    def test_get_one_user(self):
        response = app.get(USERS)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['users_list'][0]['name'], 'charlidamelio')
