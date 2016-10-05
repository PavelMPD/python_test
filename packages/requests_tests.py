import unittest
import requests


class RequestsTests(unittest.TestCase):
    def test_session(self):
        url = "https://site/login"
        session = requests.Session()
        response = session.get(url)
        self.assertEqual(response.status_code, 200)

        data = {
            "username": "",
            "password": ""
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        response = session.post(url, data=data, headers=headers)
        self.assertEqual(response.status_code, 200)
